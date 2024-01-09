#!/usr/bin/python3
import cmd

class MyConsole(cmd.Cmd):
    def do_greet(self, line):
      pass
        
if __name__ == "__main__":
    MyConsole().cmdloop()
