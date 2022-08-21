# CS 253 WEb Security

## **Assignment 2 – Oh What a Tangled Web We Weave**

This is my attempt to solve Assignment 2 for CS 253 class at Stanford

### Code Injection

1. You and a friend built a site that accepts and displays user-generated content. You recently read the XKCD comic about code injection which made you realize that you're not sanitizing user-submitted data anywhere in your web app. You realize that you're almost certainly vulnerable to Cross site scripting (XSS) and SQL injection attacks – yikes!

   Rereading the comic, you notice it ends with the phrase "I hope you've learned to sanitize your database inputs". Your friend suggests solving the issue by escaping all user-submitted data before inserting it into the database. Your friend argues that by sanitizing the inputs to the database as the comic suggests, the data can then be extracted from the database and safely used in HTML and SQL without further escaping.

   Is this a valid argument? (Yes/No) Why or why not?

   ***

   Answer:

   Validation should always be done on the way out of the database, because you won't necessarly know in what context the content will be later used.

   Different contexts have different special chars that need to be escaped

2. You and a friend decide to build an internal dashboard that will show real-time HTTP requests that are being sent by visitors to your site. The dashboard displays information about each HTTP request received by the web server, including the client's IP address, HTTP method, URL, query parameters, referrer URL, and user agent name.

   Incidentally, this is the exact set of information that most popular web servers like Nginx or Apache print into the server log files. Here is what one line from such a log file looks like:

   ```yml
   12.34.56.78 - - [17/Oct/2019:05:01:59 +0000] "GET /api/midi/search?q=hi&page=0 HTTP/1.0" 200 178 "https://example.com/search?q=h" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
   ```

   The internal dashboard will only be used by you and your friend and will not be exposed to the broader internet since the logs reveal information about your site visitors. Your friend argues that there is no need to worry about XSS vulnerabilites in an internal-only dashboard since neither of you would create an XSS attack to use against the other. Given that, they see no way that an XSS attack could occur.

   Is this a valid argument? (Yes/No) Why or why not?

   ***

   Answer:

   No, an attacker could maybe provide a payload in the query parameters at the end of the URL, or maybe forge a request and put malicious code in the User-Agent, and then the system would be compromised

   Is this a reference to log4j?

3. Name a real-world case where adherence to the Robustness principle (a.k.a. Postel's law) caused a system to have worse security. Explain how the Robustness principle led to the system having worse security properties.

   ***

   Answer:

   Postel's law states that the output of our porgram should follow some guidelines, but the program itself shoul accept non-conforming input, as long as the intention is clear.

   Like when a browser states that a `<script>` tag means a script starts, but it also accepts `<ScrIPT>`, leading to a much bigger space of possible XSS attacks.

   Another answer could include [this](https://en.wikipedia.org/wiki/Robustness_principle#cite_note-6:~:text=In%202018%2C%20a%20paper%20on%20privacy%2Denhancing%20technologies%20by%20Florentin%20Rochet%20and%20Olivier%20Pereira%20showed%20how%20to%20exploit%20Postel%27s%20robustness%20principle%20inside%20the%20Tor%20routing%20protocol%20to%20compromise%20the%20anonymity%20of%20onion%20services%20and%20Tor%20clients.%5B6%5D) part of Wiki, focusing on the Tor paper.

### Same Origin Policy

4. Name three ways that the Same Origin Policy protects a website.

   ***

   Answer:

   - A site can't get the cookies of another
   - A site can't alter the contents of another
   - A site can't send a request to another in the name of the current user

5. Can JavaScript code running on **attacker.com** cause a GET request to be sent to a URL on **victim.com**? (Yes/No)

   ***

   Yes, **GET** requests are accepted by SOP

6. Can JavaScript code running on attacker.com use the fetch() API to send a GET request to victim.com and read the HTTP response body? (Yes/No)

   ***

   No, when no CORS headers are enabled

7. Can JavaScript code running on **attacker.com** submit a form that sends a POST request to **victim.com**? (Yes/No)

   ***

   No

8. A fascinating Same origin policy "bypass" was described in ["Cross-Origin JavaScript Capability Leaks: Detection, Exploitation, and Defense"](https://www.usenix.org/conference/usenixsecurity09/technical-sessions/presentation/cross-origin-javascript-capability-leaks), a talk at USENIX '09 (one of the top security conferences). How could an attacker use this browser implementation bug to bypass the same origin policy? What was the key, underlying reason for the bug? What was the proposed mitigation? Please keep your answer to 200 words or fewer.

   ***

   TODO:

### Content Security Policy

Content Security Policy (CSP) is one of the best ways to protect your site against XSS. A properly written CSP can **completely** protect your site from reflected and stored XSS attacks, even in the presence of a bug that allows the attacker to add their own HTML code to the site.

For all questions, you should assume the user agent is a modern browser that supports the latest Content Security Policy specification, [CSP Level 3](https://www.w3.org/TR/CSP3/).

You may find these resources useful:

- [MDN: Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)
- [MDN: `Content-Security-Policy` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy)

9. An attacker takes advantage of a vulnerability in your site to inject an XSS payload into the HTML page sent by your server. Fortunately, you set up a CSP in case this happened because you follow a defense-in-depth security approach.

   Would the following CSP prevent the XSS attack? (Yes/No)

   Why or why not?

   ```http
   Content-Security-Policy: script-src 'self';
   ```

   ```html
   <script>
     alert(document.cookie);
   </script>
   ```

   ***

   Answer:

   Yes, because it's an inline script, and they are blocked by default

10. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: default-src *; script-src 'self';
    ```

    ```html
    <script>
      alert(document.cookie);
    </script>
    ```

    ***

    Yes, `default-src` is a fallback and since the script-src is defined, it behaves as the previous one

11. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: default-src 'none'; script-src 'self' 'unsafe-eval'; connect-src 'self'; img-src 'self'; style-src 'self';
    ```

    ```html
    <script>
      alert(document.cookie);
    </script>
    ```

    ***

    Yes, `unsafe-eval` works for the `eval()` runnibg scripts, this is still an inline-script

12. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: default-src 'none'; script-src 'self' 'unsafe-eval'; connect-src 'self'; img-src 'self'; style-src 'self';
    ```

    ```html
    <script>
      eval("alert(document.cookie)");
    </script>
    ```

    ***

    **Yes**, it's still an inline script after all

13. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: default-src *; script-src 'self'; connect-src *; img-src *; style-src *;
    ```

    ```html
    <script src="https://attacker.com/xss.js"></script>
    ```

    ***

    Yes, `script-src` is defined so it doesn't fallback to `default-src`

14. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: default-src 'none'; script-src 'self' https:; connect-src 'none'; img-src 'none'; style-src 'none';
    ```

    ```html
    <script src="https://attacker.com/xss.js"></script>
    ```

    ***

    No, `script-src` is set to accept `https:` like sources

15. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: script-src 'self' 'nonce-R28gU3RhbmZvcmQh';
    ```

    ```html
    <script>
      alert(document.cookie);
    </script>
    ```

    ***

    Yes, because the script needs that nonce

16. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: script-src 'self' 'nonce-R28gU3RhbmZvcmQh';
    ```

    ```html
    <script nonce="xss">
      alert(document.cookie);
    </script>
    ```

    ***

    Yes, because the nonce is wrong

17. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: script-src 'self' 'nonce-R28gU3RhbmZvcmQh' 'unsafe-inline';
    ```

    ```html
    <script nonce="xss">
      alert(document.cookie);
    </script>
    ```

    ***

    No, because of the `unsafe-inline` source

18. Would the following CSP prevent the XSS attack? (Yes/No)

    Why or why not?

    ```http
    Content-Security-Policy: script-src 'self';
    ```

    ```html
    <script src="/api/echo?str=alert(document.cookie)"></script>
    ```

    Where `/api/echo` is a working API endpoint on the victim webserver that replies back with whatever string it receives in the `str` query parameter. For example, the URL `/api/echo?str=hello` returns an HTTP response with a body of `hello`.

    In case it makes a difference, you can assume the API response has a `Content-Type` header with a value of `text/plain`.

    ***

    No, since the script is on the victim's machine. How that query can be exploited, I am not sure.

    Maybe the backend can still be tricked through it, but if it's escaped correctly when it gets to us in the current page, we should be good.

    PS. On another though, the script will be seen as that string, so our page will execute it, since we produce it.

19. Assume that **victim.com** is protected with the following CSP:

    ```http
    Content-Security-Policy: script-src 'self' 'nonce-<nonce-value-here>';
    ```

    The operator of **attacker.com** attempts to subvert **victim.com**'s CSP by visitng **victim.com** and copying the nonce they observe in the CSP header into their XSS attack payload:

    ```html
    <script nonce="<nonce-value-here>">
      alert(document.cookie);
    </script>
    ```

    Would the CSP prevent the XSS attack? (Yes/No) Why or why not?

    (Assume that **victim.com** has properly implemented their CSP nonces.)

    ***

    Yes, the nonce, if implemented properly, should be used only once per http reqest and generated in a good enough way that the attacker can't guess it

20. Read the paper ["CSP Is Dead, Long Live CSP! On the Insecurity of Whitelists and the Future of Content Security Policy"](https://ai.google/research/pubs/pub45542). Explain the problem that `'strict-dynamic'` keyword solves.

    ***

    [This](https://content-security-policy.com/strict-dynamic/) explains it well, a script that is loaded with a nonce can then load additional scripts inside the page

### Session Attacks

21. How does adding the `SameSite=Lax` cookie attribute protect a website against CSRF attacks? Give a concrete example of an attack scenario that it prevents.

    ***

    From [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite)

    > Cookies are not sent on normal cross-site subrequests (for example to load images or frames into a third party site), but are sent when a user is navigating to the origin site (i.e., when following a link).

22. Why is it important to not only delete the user's session cookie when they log out, but to also delete the session on the server side (i.e. delete it from the database)? Specifically, what could an attacker do if a server didn't delete the session on the server side after logout?

    ***

    The attacker, if it holds the cookie for that user, can still impersonate him, since from the server view, that user it's still logged in.

### Fingerprinting

23. Explain how a tracker could use third-party cookies and an image request to a `pixel.gif` image to identify a user on two separate domains.

    ***

    The slides from Brave talk shows an example, you can get an image from `example.com` while visiting `1.com`, at that moment `example.com` sets a `cookie=123`, the second time you are on `2.com` and request something from `example.com`, `example.com` sees that cookie set and can figure out you were on both sites

24. Explain how "partitioning" or "double-keying" the browser storage (such as cookies and `localStorage`) helps to prevent web tracking. What tracker behavior does it prevent? How does double-keying prevent this behavior?

    ***

    Third party storage is not shared across sites
