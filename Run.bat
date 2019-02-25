set Ud=32.768
set population=100
set dim=100
set F=0.3
set CR=0.1
set iteration=400

del *.txt

python main.py %Ud% %population% %dim% %F% %CR% %iteration% >> %population%_%dim%_%F%_%CR%_%iteration%.txt

pause