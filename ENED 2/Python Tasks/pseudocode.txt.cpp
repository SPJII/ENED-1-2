// This program selects Player 1 or Player 2 at random 
program RandomPlayer;
uses crt;
var
   Player: integer;
begin
    randomize;
    Player := random(2) + 1;
    if Player = 1 then
        writeln('Player 1')
    else
        writeln('Player 2');
    readkey;
    end.