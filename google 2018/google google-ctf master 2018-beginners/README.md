# Google CTF 2018 Beginners Quest

- The website isn’t available anymore, we can still find the files in third party repos, I use this one : [https://github.com/danicrg/ctf-writeups/tree/5de10a7a42464dce51499bb3e31979013f5f0cf5/googleCTF](https://github.com/danicrg/ctf-writeups/tree/5de10a7a42464dce51499bb3e31979013f5f0cf5/googleCTF)
- This guy solves all the challanges and explains them as he goes [https://youtu.be/qDYwcIf0LZw](https://youtu.be/qDYwcIf0LZw)

## Misc Letter

- Super easy, we have to just copy the text that is hidden in pdf
- **CTF{ICanReadDis}**

## Misc OCR is COOL

- We get a photo that has a ceaser cipher in it
- We don’t want to copy all of the email by hand, we can use an ocr software
- a quick search gives us this **sudo apt install tesseract-ocr**
- Then it’s just running the command : **tesseract OCR_is_cool.png output -l eng**
- We then get an output.txt that has the text, more or less accurate, but we put it in CyberChef[[https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,7)&input=Vk1Ze3Z0eGl0a3ZiaWF4a2JsdGludWxtYm1ubWJoZ3ZiaWF4a30](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,7)&input=Vk1Ze3Z0eGl0a3ZiaWF4a2JsdGludWxtYm1ubWJoZ3ZiaWF4a30)] try a few different ROTn and 7 seems to work, we find a section like CTF{…} that is almost the flag
- We can just copy the section from the png that is enclosed in {} and put it through ROT7, and we will get the flag: **CTF{caesarcipherisasubstitutioncipher}**

## Misc Floppy

- Somehow i solved this one solo
- It’s just a foo.ico file in here, running strings doesn’t show anything, neither does file
- WE open it in a hex editor, ([ImHEX](https://github.com/WerWolv/ImHex)) and it shows some interesting things, we see suff like data.txt
- I’ve opened wiki to try to look at the .ico file specs, but tried to find a stego tool first, then i found this site [https://0xrick.github.io/lists/stego/#tools](https://0xrick.github.io/lists/stego/#tools) , it gives some cool tools, but the most important **binwalk**
- Seeing the ImHex output again, we see some PK headers, which means there is a zip archive in there
- running binwalk -e foo.ico , it finds some files, including **driver.txt**
- Never the less, it has out flag in it **CTF{qeY80sU6Ktko8BJW}**

## PWN Moar

- These are a little bit shitty, since i have to run them locally
- we get a [moar.sh](http://moar.sh) and a disable_dmz.sh , we run moar.sh, and the pawnable server is localhost
- we try to run the command nc 127.0.0.1 1337 and connect to the “server”
- it is the man page of socat, we can run commands in that env with !
- like !cat flag will cat the file flag
- we dont have a file like this, but the disable_dmz.sh has the flag in it
- we can just run !cat disable_dmz.sh and see what is in it
- **CTF{SOmething-CATastr0phic}**
- Now, i know where the flag was because i had the server locally, but we could’ve just cd and ls all the files, and find it eventually, in the original challnage it was in /home/moar, so not very hidden

## MISC Floppy2

## MISC Security by Obscurity

## WEB JS safe

## RE Firmware

## WEB Router-UI

## PWN-RE AdminUI 1

## PWN-RE AdminUI 2

## PWN-RE AdminUI 3

## PWN Message of the day

## RE Gatekeeper

## MISC Media-db

## PWN Poetry

## PWN Filter ENV

## PWN Fridge Todo List

## PWN Holey Beep