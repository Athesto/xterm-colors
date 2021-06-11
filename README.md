# XTERM colors

## How to use
 - Download the script
```
curl -sLo colors github.com/Athesto/xterm-colors/raw/main/script.py
chmod u+x colors
./colors --help
```
## EscapeCodes
```
echo -e "\e[3{16-color}m4BIT COLOR\e[0m"
echo -e "\e[38;5;{256-color}m8BIT COLOR\e[0m"
echo -e "\e[38;2;{red};{green};{blue}m24BIT TRUE COLOR\e[0m"

echo -e "\e[31mRED\e[0m"
echo -e "\e[38;5;161mRASPBERRY\e[0m"
echo -e "\e[38;2;255;128;0mORANGE\e[0m"
```
### Alternaives to \e
`\e` is the escape character but you can use any of its representations
```
(char) \e 
(octa) \033 \0033
(hexa) \x1b \x01b \x001b
(unic) \u1b \u01b \u001b

echo -e "\u01b[32mGREEN\e[0m"
```


## GRAY-SCALE
|value |   HEX   |DEC  |
|:----:|---------|:---:|
|0     | 0x080808|8|
|0     | 0x080808|8|


![imagecodes]
# Links
 - [ANSI escape codes][wiki_ansi]
 - [Flozz' Tutorial][tuto_flozz]
 - [Interactive view, ANSI][dynamic_1]
 - [True colors, gist][gist_trueColors]
 - [Tutorial ANSI codes][tuto_ansi1]
 - [Escape Codes][list_esc]

http://yjlv.blogspot.com/2013/02/terminal-256-colors-scripts.html
https://lh3.googleusercontent.com/proxy/szAMlToc8VSdZGQy3w1jn9fXVGOdgBxjeAEMpQKFUv06JRVnQN3PBwNWFmM6GuatFQlyOB2LMLhVGz5Jvg8QbQlS
https://terminalguide.namepad.de/attr/fgcol256/
https://stackoverflow.com/questions/22991809/how-to-produce-rgb-cube-matrix-in-python
https://wholeo.net/Caroling/channel/akasha/akashicRecord/colorAccess/colorCubes2.htm
https://terminalguide.namepad.de/attr/fgcol256/colors.png
https://www.youtube.com/watch?v=wqZKhoDP0fU
https://www.google.com/search?q=256+wheel+color&sxsrf=ALeKk00UitW2HnSbdXeYFTeMwcC8F1iqUw:1605563615407&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj5n9fHhojtAhUnWN8KHRb4BcwQ_AUoAXoECBcQAw&biw=1366&bih=637
https://www.loriswebs.com/websafecolors.html
https://twitter.com/codigodecolores?lang=es
https://github.com/feluxe/sty
https://lab.lilydjwg.me/articles/vim-color-modified.html

<!--links-->
[imagecodes]:assets/xterm256.png
[wiki_ansi]:https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_parameters
[tuto_ansi1]:https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
[tuto_flozz]:https://misc.flogisoft.com/bash/tip_colors_and_formatting
[dynamic_1]:http://the-light.com/colclick.html
[gist_trueColors]:https://gist.github.com/sindresorhus/bed863fb8bedf023b833c88c322e44f9
[list_esc]:https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
