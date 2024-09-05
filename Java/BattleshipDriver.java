import java.util.Scanner;
public class BattleshipDriver
{

    public static void main(String[] args)
    {

        
        Scanner input = new Scanner(System.in);
        System.out.println("How many torpedoes would you like to start with? (Recommended: 50)");
        int numTorpedoes = input.nextInt();
        input.nextLine();

        Battleship game = new Battleship(numTorpedoes);
        game.printWelcome();
        game.printBoard(false);
       
        while(game.keepPlaying())
        {
            System.out.println("Please enter your coordinates:");
            String coords = input.nextLine();
            game.fire(coords);
            game.printBoard(false);
        }
        
        if(game.hasWon())
        {
            game.printBoard(true);
            System.out.println("Congratulations, you win!");
            input.close();
        }
        else
        {
            game.printBoard(true);
            System.out.println("Sorry, you lose.");
            input.close();
        }
        
    }

}
