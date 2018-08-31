$( document ).ready(function() {
    readyPlayerOne();
    playGame();
    })

    var playerNames = []
    
    function readyPlayerOne() {
        let currentPlayer = Math.round(Math.random());
        let currentPlayerName = Math.round(Math.random());
            if (currentPlayerName == 0){
                playerNames.push(player1)
                playerNames.push(player2)
            }else{
                playerNames.push(player2)
                playerNames.push(player1)
            }


        if (currentPlayer === 0) {   
            let descMove = playerNames[0] + " Has first turn!!";     
            setTurnHolder("X");
            setTurnText(descMove);        
        }
        else {  
            let descMove = playerNames[1] + " Has first turn!!";         
            setTurnHolder("O");    
            setTurnText(descMove);    
        }

    }
    
    function playGame() {    
        let currentPlayer = document.getElementById("turnHolder").innerHTML;    
        let playerOh = new Array();
        let playerX = new Array();        
        getMove(currentPlayer, playerOh, playerX);
    }
    
    function getMove(currentPlayer, playerOh, playerX) {

        let numMoves = 0;    
        let currentSquare = "square10";            
        $(".grid").mousedown(function(){        
            currentSquare = ($(this).attr('id'));        
            let text = ($(this).html());
              
            if (text === '&nbsp;') {            
                document.getElementById(currentSquare).innerHTML = currentPlayer;
                                            
                if (currentPlayer === "O" ) {
                    playerOh.push(currentSquare);                    
                    checkWin(playerOh, currentPlayer, numMoves);
                    currentPlayer = 'X';     
                    setTurnText(playerNames[0] + " Has Next Move!!!");           
                }
                else {
                    playerX.push(currentSquare);                    
                    checkWin(playerX, currentPlayer, numMoves);
                    currentPlayer = 'O';
                    setTurnText(playerNames[1] + " Has Next Move!!!");
                }
                numMoves = (playerOh.length + playerX.length);
                checkDraw(numMoves);
                
                setTurnHolder(currentPlayer);                
            }
            else {
                alert('Not a valid move!');
            }
                    
        });
        
    }
    
    function checkDraw(numMoves){
        if (numMoves === 9) {
            alert("Draw! Try Again!!!");
            location.reload();

        }
    }

    function checkWin(moves, currentPlayer) {
        
        let winComb = new Array (0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 3, 6, 1, 4, 7, 2, 5, 8, 2, 4, 6, 0, 4, 8);        
        let winningComb = [];        
        let match = [];
        let numMatch = moves.length;
        let currentTemp = "";
        let winTemp = "";      

        for (var n=0; n<8; n++){
            winningComb[n] = [];
            for (var i=0; i<3; i++) {
                let winNextNo = "square" + winComb.shift();
                winningComb[n].push(winNextNo);
            }            
        }
        

        for (var c=0; c<8; c++) {
            match = [];                        
                  
            for (var f=0; f<3; f++){
                for (var d=0; d<numMatch; d++){
                    if (winningComb[c][f] === moves[d]){
                        winTemp = moves[d];
                        match.push(winTemp);
                        currentTemp = match.length;
                        if (currentTemp > 2) {
                            setTurnHolder(currentPlayer);
                            var winning_player = "";
                            if (currentPlayer == 'X'){
                                var winning_player = playerNames[0];
                            }else{
                                var winning_player = playerNames[1];
                            }
                            alert(currentPlayer + " " + winning_player + " HAS WON!!!"); 
                            setTurnText(winning_player + " HAS WON!!!");   
                            var x = document.getElementById("playagainbtn"); 
                            x.style.display = "block";                       
                            var y = document.getElementById("submitScoreBtn"); 
                            y.click();
                        }
                        
                    }

                }
                
            }
            
  
            }           
        }
    
        function playagain(){
            location.reload();
        }
        
    
    function setTurnText(descMove) {
        $('#turnText').html("   " + descMove);
    }
    
    function setTurnHolder(descTurn) {
        $('#turnHolder').html(descTurn);
    }
    
       