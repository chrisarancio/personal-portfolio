import java.util.ArrayList;
public class Battleship
{
    public static final int BOARD_SIZE = 10;
    public static final String SPACE_OPEN = " ";
    public static final String SPACE_MISS = "-";
    public static final String SPACE_HIT = "#";
    
    private int startingAmmunition;
    private ArrayList<Ship> allShips = new ArrayList<Ship>();
    private static int numHits = 0;
    
    private String[][] board = new String[10][10];
    
    /**
     * This is the constructor for the battleship game.
     * @param startingAmmunition
     */
    public Battleship(int startingAmmunition)
    {
        this.startingAmmunition = startingAmmunition;
        
        for(int row = 0; row < BOARD_SIZE; row++)
        {
            for(int col = 0; col < BOARD_SIZE; col++)
            {
                board[row][col] = SPACE_OPEN;
            }
        }
        makeShips();
    }
    /**
     * This method is called by the battleship constructor and initializes the name
     *  and size of every ship. It then calls the hide method to assign row and column 
     *  values for each ship.
     */
    private void makeShips()
    {
        Ship carrier = new Ship("Carrier", 5);
        allShips.add(carrier);
        
        Ship battleship = new Ship("Battleship", 4);
        allShips.add(battleship);
       
        
        Ship destroyer = new Ship("Destroyer", 3);
        allShips.add(destroyer);
        
        
        Ship submarine = new Ship("Submarine", 3);
        allShips.add(submarine);
        
        
        Ship patrolBoat = new Ship("Patrol Boat", 2);
        allShips.add(patrolBoat);
        
        Ship.hide(allShips);
    }
    
    /**
     * This returns the amount of ammunition remaining.
     * @return this returns the amount of ammunition remaining.
     */
    public int getAmmunition()
    {
        return startingAmmunition;
    }
    
    /**
     * This method will print out the battleship board. If reveal is false, then 
     * is will print out the board with the current hits and misses. If reveal is 
     * true, then is will print out the board wit the first letter of each ship in 
     * its correct position. An upper case letter indicates a hit and a lower case letter 
     * indicates a miss.
     * @param reveal this is a boolean of whether the ships locations should be 
     * revealed to the player
     */
    public void printBoard(boolean reveal)
    {
        System.out.print("  ");
        for(int i = 1; i <= BOARD_SIZE; i++)
        {
            System.out.print("| " + i + " ");
        }
        System.out.print("|\n");
        
        for(int row = 0; row < 10; row++)
        {
            for(int col = 0; col < 10; col++)
            {
                if(col == 0)
                {
                    System.out.print((char)(65 + row) + " ");
                }
                if(reveal)
                {
                    for(int i = 0; i < allShips.size(); i++)
                    {
                        Ship currShip = allShips.get(i);
                        int printCol = currShip.getShipCols().get(0);
                        int printRow = currShip.getShipRows().get(0);
                        
                        if(currShip.getShipRows().size() > currShip.getShipCols().size()) //Checks if ship is vertical
                        {
                            for(int j = 0; j < currShip.getSize(); j++)
                            {
                                
                                //If board[row][col] has a # then print capital letter
                                if(board[printRow + j][printCol] == SPACE_HIT)
                                {
                                    board[printRow + j][printCol] = currShip.getName().substring(0,1).toUpperCase();
                                }
                                else if(board[printRow + j][printCol] == SPACE_OPEN)
                                {
                                   board[printRow + j][printCol] = currShip.getName().substring(0,1).toLowerCase();
                                }
                            }
                        }
                        else
                        {
                            for(int j = 0; j < currShip.getSize(); j++)
                            {
                                
                                if(board[printRow][printCol + j] == SPACE_HIT)
                                {
                                    board[printRow][printCol + j] = currShip.getName().substring(0,1).toUpperCase();
                                }
                                else if(board[printRow][printCol + j] == SPACE_OPEN)
                                {
                                   board[printRow][printCol + j] = currShip.getName().substring(0,1).toLowerCase();
                                }
                            }
                        }
                    }
                }
                System.out.print("| " + (board[row][col]) + " ");
                
            }
            System.out.print("\n");
            System.out.print("--+");
            for(int i = 0; i < BOARD_SIZE; i++)
            {
                System.out.print("---+");
            }
            System.out.print("\n");
        }
    }
    
    
    /**
     * This function is called after a successful hit and reads the health of a
     * ship and determines if the ship was sunk. If so, it prints out a message
     * to the console reading "You sunk my ...!"
     * @param name
     */
    public void printSunkMessage(String name)
    {
        String message = "\nYou sunk my ";
        message += (name + "!\n");
        System.out.println(message);
    }
    
    /**
     * This prints out the text at the start of the game.
     */
    public void printWelcome()
    {
        String text = "***************************\n"
                + "*  WELCOME TO BATTLESHIP  *\n"
                + "***************************\n"
                + "\n"
                + "Five enemy ships are reported to be hidden in the water.\n"
                + "You must find and sink them all to save the day!\n"
                + "Fire wisely, you only have limited torpedos in your hold.\n"
                + "\n"
                + "Enter coordinates as: [LETTER][NUMBER]\n"
                + "For example, the top-left square is A1\n"
                + "\n"
                + "Good luck!\n";
        System.out.println(text);
    }
    
    /**
     * This checks whether the player has run out of ammunition.
     * @return whether the player has any ammunition left
     */
    public boolean keepPlaying()
    {
        if(hasWon() || startingAmmunition == 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    
    /**
     * This checks if the player has won the game.
     * @return whether the player has hit and sank every ship
     */
    public boolean hasWon()
    {
        if(numHits == 17)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    
    /**
     * This takes user input and determines whether the player has hit a ship or not
     * @param location this is the user input in the format [Letter][Number].
     */
    public void fire(String location)
    {
        boolean hit = false;
        String rowLetterString = location.substring(0, 1).toUpperCase();
        char rowLetterChar = rowLetterString.charAt(0);
        int rowNumber = (int)rowLetterChar - 65;
        
        String columnString = location.substring(1);
        int colNumber = Integer.parseInt(columnString) - 1;
        
        int currShip = 0;
        while(currShip < 5)
        {
            if(allShips.get(currShip).checkLocation(rowNumber, colNumber))
            {
                board[rowNumber][colNumber] = SPACE_HIT;
                hit = true;
                startingAmmunition--;
                numHits++;
                
                // The below section prints a special message if a ship was sunk
                int currHealth = allShips.get(currShip).getHealth();
                if (currHealth > 1)
                {
                    allShips.get(currShip).setHealth(currHealth-1);
                }
                else
                {
                   printSunkMessage(allShips.get(currShip).getName());
                }
                
                break;
            }
            else
            {
                currShip++;
            }
        }
        if(hit == false)
        {
            board[rowNumber][colNumber] = SPACE_MISS;
            startingAmmunition--;
        }
    }
}
