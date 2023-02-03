print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

dir_1 = input('Choose between "Left" or "Right" ?\n').lower()
if dir_1 == "left":
    print('\nGreat! You took the Right pathway going to the Left')

    print('''
                  _
             .''.' \    _  __
 ___         './    '. ' `'  `
    '._______.'       \
                       '.__________
                                   '-.____________
 _________________________________________________'.__________________
                                      ____________.'
                         __________.-'
      _______          .'                      Sarah Day
 ___.'       '.       /               '-._         medieval@micron.net
             .'\    .' ._,.__,        ____\____.o.
             '..'._/                 '-._______.-'
                                     .-'_______'-.
                                         _/    'o'
                                      .-'
    ''')
    dir_2 = input(
        '\nYou have come to a lake, There is an island in the middle of the Lake.\nChoose between you want to "Swim" the Lake or "Wait" for the Boat ?\n').lower()
    if dir_2 == "wait":
        print('''
                            `-._-.  `.
                                `.`-.\`.
                                   ) )) )
                                  / /( (
                                 ( (  \ \
                                  ) )  ) )
                                 (  \ ( (
                                  )_/  `,)
                                  |:|  |:|
                                  |'|  |'|
                                  |.|  |.|
                                 _| |__| |________________
                                 >| |--| |------.-.-----.-`
                                 ||.|::|.| - =- |:|-=  -;
                                 ||:||||:|  -   '-' -=_/
            .-::=::=::===::==::==++-++++-| =  _= -=  -/
            |_||_||_||___||__||__||:||||||_-____-__=_/
            |,-/-/-.|,-------.|,--.|,---.|,---.|,-|\|
            |:/-/.:.|- _.-. =-|  -=| -=  |-_ = |- |||__ _  __
   _______ _|/-/.:. | =_|:|_  |=-  |-  _=|    -| =|||_..-'`:;'
   \:::'`.``'-/.:._.|___|:|_-=|__-_|_=-__|_-=_.:.-''  . ..:/
    `::.`. .` . `   `     . `  . `     . `    `  `. .`..::/
      `;::.`. .` .`  .`  `    `    `  `    `  .  ` . `..:/
 ~  ~~/;;;::._..__`____._`___.__`___.___`__._``_.._.::`:( ~~
  ~        ~          ~                  ~      ~~
     ~        ~              ~~   ~~        ~  ~     ~    ~
            ~     ~      ~ ~         ~            ~~
               ~SSt~     ~        ~~         ~
        ''')
        print("\nGreat ! Welcome Aboard, let me help you cross this Crocodile Lake on my Boat.")

        dir_3 = input(
            'Voila ! You are just one Door away from your Treasure.\nChoose between the Colour of the Door as "Red","Blue" or "Yellow" ?\n').lower()
        if dir_3 == "yellow":

            print('''          
            _,-""._                       
        _,-",~@);%~`-._               
        \\""""""------"-...___         
         |""""""------/|      |     
         |      |HHHHH||      |       
         |""""""------||      |       
         |      _____ ||      |        
         |     : ___ :||      |        
         |     :|GSN|:||      |         
         |     :|___|:||      |        
         |     :""""":||      |          
         |"""""-------||      |         
         || ,~@);~.  |||      |        
         ||~  ===  ~ |||      |        
         |"""""-------||      |         
         |"""""-------||      |         
         || ,~@);~.  |||      |       
         ||~  ===  ~ |||      |       
         |"""""-------||      |      
        /""""""-------\\....___\      
     jm """""""---------....___: 
            ''')

            print("\nCongratulations on Winning the Game.\nYou May take your Treasure and Use it in Good Cause")

        else:
            print('''
                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 -sjm
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``
            ''')
            print("\nGame Over, That door has a Dangerous Dragon Inside.")
    else:
        print('''
                     _.---._     .---.
            __...---' .---. `---'-.   `.
  ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
 -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
  ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
    ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
     ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
         ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
       jgs   ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                     ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~
        ''')
        print("\nGame Over, The Lake is filled with Hungry Crocodiles. You Should have waited.")
else:
    print('''

           ,aodObo,
        ,AMMMMP~~~~
     ,MMMMMMMMA.
   ,M;'     `YV'
  AM' ,OMA,
 AM|   `~VMM,.      .,ama,____,amma,..
 MML      )MMMD   .AMMMMMMMMMMMMMMMMMMD.
 VMMM    .AMMY'  ,AMMMMMMMMMMMMMMMMMMMMD
 `VMM, AMMMV'  ,AMMMMMMMMMMMMMMMMMMMMMMM,                ,
  VMMMmMMV'  ,AMY~~''  'MMMMMMMMMMMM' '~~             ,aMM
  `YMMMM'   AMM'        `VMMMMMMMMP'_              A,aMMMM
   AMMM'    VMMA. YVmmmMMMMMMMMMMML MmmmY          MMMMMMM
  ,AMMA   _,HMMMMmdMMMMMMMMMMMMMMMML`VMV'         ,MMMMMMM
  AMMMA _'MMMMMMMMMMMMMMMMMMMMMMMMMMA `'          MMMMMMMM
 ,AMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMa      ,,,   `MMMMMMM
 AMMMMMMMMM'~`YMMMMMMMMMMMMMMMMMMMMMMA    ,AMMV    MMMMMMM
 VMV MMMMMV   `YMMMMMMMMMMMMMMMMMMMMMY   `VMMY'  adMMMMMMM
 `V  MMMM'      `YMMMMMMMV.~~~~~~~~~,aado,`V''   MMMMMMMMM
    aMMMMmv       `YMMMMMMMm,    ,/AMMMMMA,      YMMMMMMMM
    VMMMMM,,v       YMMMMMMMMMo oMMMMMMMMM'    a, YMMMMMMM
    `YMMMMMY'       `YMMMMMMMY' `YMMMMMMMY     MMmMMMMMMMM
     AMMMMM  ,        ~~~~~,aooooa,~~~~~~      MMMMMMMMMMM
       YMMMb,d'         dMMMMMMMMMMMMMD,   a,, AMMMMMMMMMM
        YMMMMM, A       YMMMMMMMMMMMMMY   ,MMMMMMMMMMMMMMM
       AMMMMMMMMM        `~~~~'  `~~~~'   AMMMMMMMMMMMMMMM
       `VMMMMMM'  ,A,                  ,,AMMMMMMMMMMMMMMMM
     ,AMMMMMMMMMMMMMMA,       ,aAMMMMMMMMMMMMMMMMMMMMMMMMM
   ,AMMMMMMMMMMMMMMMMMMA,    AMMMMMMMMMMMMMMMMMMMMMMMMMMMM
 ,AMMMMMMMMMMMMMMMMMMMMMA   AMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
AMMMMMMMMMMMMMMMMMMMMMMMMAaAMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

    ''')
    print("\nGame Over, you went to the Lion's Forest")

input("Press Enter to End the Program !!!")