public class CodeTester
{
    private static final String[] ROWS = { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J" };

    public static void main(String[] args)
    {
        Battleship game = new Battleship(90);
                
                game.printWelcome();
                game.printBoard(false);
                game.printBoard(true);
                
                outer:
                for (int row = 0; row < ROWS.length; row++)
                {
                    for (int col = 0; col < Battleship.BOARD_SIZE; col++)
                    {
                        game.fire(ROWS[row] + (col + 1));
                        if (!game.keepPlaying())
                        {
                            break outer;
                        }
                    }
                }
                
                if (game.hasWon())
                {
                    System.out.println("WIN");
                }
                else
                {
                    System.out.println("LOST");
                }
                System.out.println("Remaining torpedos: " + game.getAmmunition());
        
                game.printBoard(false);
                game.printBoard(true);

    }

}
