import cx_Freeze

executables = [ cx_Freeze.Executable ("SNAKE.py",
                                    base = "Win32GUI") ]

build_exe_options = {"packages" : [ "pygame" ],
"include_files" : [ "bite.ogg",
                    "game_loop.ogg",
                    "game_over.ogg",
                    "GAME_PLAY.jpg",
                    "icon.png",
                    "INSTRUCCIONES.jpg",
                    "INTRO.jpg",
                    "PAUSA1.jpg",
                    "PERDISTE.jpg",
                    "select.ogg"
                    ]}

cx_Freeze.setup(
    name = "SNAKE",
    version = "3.0",
    description = "Un juego rudimentario.",
    options = {"build_exe": build_exe_options},
    executables = executables

)
