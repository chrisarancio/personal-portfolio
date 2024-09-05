import java.util.ArrayList;
public class Ship
{
    private String name;
    private int size;
    private int health;
    private ArrayList<Integer> shipRows = new ArrayList<Integer>();
    private ArrayList<Integer> shipCols = new ArrayList<Integer>();
    private boolean isHorizontal;
    /**
     * Construct a ship
     * @param name the name of ship
     * @param size the size of ship
     */
    public Ship(String name, int size)
    {
        this.name = name;
        this.size = size;
        this.health = size;
    }
    /**
     * Returns name of ship
     * @return name of ship
     */
    public String getName()
    {
        return name;
    }
    /**
     * Returns size of ship
     * @return size of ship
     */
    public int getSize()
    {
        return size;
    }
    /**
     * Returns arrayList of ship rows
     * @return the arrayList of the ships row(s)
     */
    public ArrayList<Integer> getShipRows()
    {
        return this.shipRows;
    }
    
    /**
     * Returns arrayList of ship columns
     * @return the arrayList of the ships column(s)
     */
    public ArrayList<Integer> getShipCols()
    {
        return this.shipCols;
    }
    
    /**
     * Returns boolean of whether ship is horizontal.
     * @return if the ship is horizontal
     */
    public boolean isHorizontal()
    {
        return isHorizontal;
    }
    
    /**
     * Sets the orientation of the ship
     * @param isHorizontal
     */
    public void setHorizontal(boolean isHorizontal)
    {
        this.isHorizontal = isHorizontal;
    }
    
    /**
     * This returns the current health value of the ship.
     * @return the current health of the ship
     */
    public int getHealth()
    {
        return this.health;
    }
    
    /**
     * This sets the health of the ship to the inputed value.
     * @param newHealth
     */
    public void setHealth(int newHealth)
    {
        this.health = newHealth;
    }

    
//    public void addCoords(ArrayList<Integer> rows, ArrayList<Integer> cols)
//    {
//        this.shipRows = rows;
//        this.shipCols = cols;
//    }
    /**
     * This checks to see if there is a ship at the passed in location.
     * @param row
     * @param col
     * @return if the location passed in contains a ship
     */
    public boolean checkLocation(int row, int col)
    {
        boolean rowTrue = false;
        boolean colTrue = false;
        for(int i = 0; i < shipRows.size(); i++)
        {
            if(shipRows.get(i) != null && shipRows.get(i) == row)
            {
                rowTrue = true;
                break;
            }
        }
        
        for(int i = 0; i < shipCols.size(); i++)
        {
            if(shipCols.get(i) != null && (shipCols.get(i) - 1) == (col - 1))
            {
                colTrue = true;
                break;
            }
        }
        return(rowTrue && colTrue);
    }
    
    /*This method randomizes the placement of the ships and initializes their arrayLists of shipRows
     * and shipCols to have those random values. This method also calls the checkOverlap() method to make
     * sure that the newly randomized ship would not have overlapped with a previously added ship.
     */
    /**
     * This initializes every ship to have two arrayLists of its rows and columns. None of the ships will overlap.
     * @param allShips
     */
    public static void hide(ArrayList<Ship> allShips)
    {
        int moveBackIndicator = 0;
        int totalShips = 0;
        int h = 0;
        boolean safeSpots = true;
        while(h < allShips.size())
        {
            moveBackIndicator = 0;
            Ship currShip = allShips.get(h);
            int size = currShip.getSize();

            if(Math.random() < .5) //Is horizontal
            {
                int startingRandomColNum = (int)(Math.random() * (10 - size));
                int startingRandomRowNum = (int)(Math.random() * 10);
                boolean isHorizontal = true;
                currShip.setHorizontal(true);
                if(totalShips != 0)
                {
                    safeSpots = currShip.checkOverlap(allShips, startingRandomRowNum, startingRandomColNum, totalShips, isHorizontal, size);
                }
                
                if(safeSpots)
                {
                    currShip.getShipRows().add(startingRandomRowNum);
                    for(int j = 0; j < size; j++)
                    {
                        currShip.getShipCols().add(startingRandomColNum + j);
                    }  
                        totalShips++;
                        //System.out.println("This is the curr ship rows: " + currShip.getShipRows());
                        //System.out.println("This is the curr ship cols: " + currShip.getShipCols());
                }
                else
                {
                    moveBackIndicator++;
                }
                
            }
            else
            {
                int startingRandomColNum = (int)(Math.random() * 10);
                int startingRandomRowNum = (int)(Math.random() * (10 - size));
                boolean isHorizontal = false;
                currShip.setHorizontal(false);
                if(totalShips != 0)
                {
                    safeSpots = currShip.checkOverlap(allShips, startingRandomRowNum, startingRandomColNum, totalShips, isHorizontal, size);
                }
                if(safeSpots)
                {
                    currShip.getShipCols().add(startingRandomColNum);
                    for(int j = 0; j < size; j++)
                    {
                        currShip.getShipRows().add(startingRandomRowNum + j);
                    }
                    totalShips++;
                    //System.out.println("This is the curr ship rows: " + currShip.getShipRows());
                    //System.out.println("This is the curr ship cols: " + currShip.getShipCols());
                }
                else
                {
                    moveBackIndicator++;
                }
                
            }
            if(moveBackIndicator == 1) 
            {
                h--;
            }
            h++;
        }
    }
    
    /**
     * This checks to see if any previously initialized ship overlaps with the newly randomized coordinates of the new ship.
     * @param allShips
     * @param currRow
     * @param currCol
     * @param totalShips
     * @param isHorizontal
     * @param addingShipSize
     * @return this returns a boolean if both the row and column are already occupied
     */
    public boolean checkOverlap(ArrayList<Ship> allShips, int currRow, int currCol, int totalShips, boolean isHorizontal, int addingShipSize)
    {
//        //int safeSpots = 0;
//        for(int i = 0; i < totalShips; i++)
//        {
//            Ship currShip = allShips.get(i);
//            for(int j = 0; j < currShip.getSize(); j++)
//            {
//                if(j < currShip.getShipRows().size())
//                {
//                    for(int k = 0; k < addingShipSize; k++)
//                        if(currShip.getShipRows().get(j) == currRow + k)
//                        {
//                            return false;
//                        }
//                    }
////                    if(currShip.getShipRows().get(j) != (currRow + j))
////                    {
////                        safeSpots++;
////                    }
//                
//                
//                if(j < currShip.getShipCols().size())
//                {
//                    for(int k = 0; k < addingShipSize; k++)
//                    {
//                        if(currShip.getShipCols().get(j) == currCol + k)
//                        {
//                            return false;
//                        }
//                    }
////                    if(currShip.getShipCols().get(j) != (currCol + j))
////                    {
////                        safeSpots++;
////                    }
//                }
//            }
//        }
//        return true;
//       //return safeSpots;
//       //(totalShips == 1 && safeSpots == 6) || (totalShips == 2 && safeSpots == 11) ||
//        //(totalShips == 3 && safeSpots == 15) || (totalShips == 4 && safeSpots == 19) ||
//        //(totalShips == 5 && safeSpots == 22) || totalShips == 0)
//        boolean rowGood = true;
//        boolean colGood = true;
//        if(isHorizontal)
//        {
//            ArrayList<Integer> addingShipRows = new ArrayList<Integer>();
//            ArrayList<Integer> addingShipCols = new ArrayList<Integer>();
//            addingShipRows.add(currRow);
//            for(int i = 0; i < addingShipSize; i++)
//            {
//                addingShipCols.add(currCol + i);
//            }
//            
//            for(int j = 0; j < totalShips; j++)
//            {
//                
//                Ship currShip = allShips.get(j);
//                if(currShip.isHorizontal())
//                {
//                
//                    for(int k = 0; k < addingShipRows.size(); k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipRows().get(k) != null && currShip.getShipRows().contains(addingShipRows.get(k)))
//                        {
//                            rowGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                    
//                    for(int k = 0; k < addingShipCols.size(); k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipCols().get(k) != null && currShip.getShipCols().get(k) == addingShipCols.get(k))
//                        {
//                            colGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                }
//                else
//                {
//                    for(int k = 0; k < addingShipRows.size(); k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipRows().get(k) != null && currShip.getShipRows().contains(addingShipRows.get(k)))
//                        {
//                            rowGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                    
//                    for(int k = 0; k < 1; k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipCols().get(k) != null && currShip.getShipCols().contains(addingShipCols.get(0)))
//                        {
//                            colGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                }
//            }
//        }
//        else
//        {
//            ArrayList<Integer> addingShipRows = new ArrayList<Integer>();
//            ArrayList<Integer> addingShipCols = new ArrayList<Integer>();
//            addingShipCols.add(currCol);
//            for(int i = 0; i < addingShipSize; i++)
//            {
//                addingShipRows.add(currRow + i);
//            }
//            
//            for(int j = 0; j < totalShips; j++)
//            {
//                
//                Ship currShip = allShips.get(j);
//                if(currShip.isHorizontal())
//                {
//                
//                    for(int k = 0; k < 1; k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipRows().get(k) != null && currShip.getShipRows().contains(addingShipRows.get(0)))
//                        {
//                            rowGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                    
//                    for(int k = 0; k < addingShipCols.size(); k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipCols().get(k) != null && currShip.getShipCols().get(k) == addingShipCols.get(k))
//                        {
//                            colGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                }
//                else
//                {
//                    for(int k = 0; k < addingShipRows.size(); k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipRows().get(k) != null && currShip.getShipRows().get(k) == addingShipRows.get(k))
//                        {
//                            rowGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                    
//                    for(int k = 0; k < 1; k++)
//                    {
//                        inner:
//                        {
//                        if(currShip.getShipCols().get(k) != null && currShip.getShipCols().get(k) == addingShipCols.get(k))
//                        {
//                            colGood = false;
//                            break inner;
//                        }
//                        }
//                    }
//                }
//            }
//        }
//        
//        if(rowGood == false && colGood == false)
//        {
//            return false;
//        }
//        else
//        {
//            return true;
//        }
        
        //The contains method is my savior. I was trying to reinvent the wheel this whole time. :(
        /*This method checks to see if both the row and col are occupied for the randomized points of
        *a new ship. It iterates through the arrayLists of shipRows and shipCols of the ships that have
        *already been added and checks to see if they contain both the same row and col. This would mean
        *that there is a point where a new added ship would overlap.
        */
        boolean rowGood = true;
        boolean colGood = true;
        if(isHorizontal)
        {
            ArrayList<Integer> addingShipRows = new ArrayList<Integer>();
            ArrayList<Integer> addingShipCols = new ArrayList<Integer>();
            addingShipRows.add(currRow);
            for(int i = 0; i < addingShipSize; i++)
            {
                addingShipCols.add(currCol + i);
            }
            
            for(int j = 0; j < totalShips; j++)
            {
                Ship currShip = allShips.get(j);
                for(int k = 0; k < addingShipRows.size(); k++)
                {
                    inner:
                    {
                    if(currShip.getShipRows().contains(addingShipRows.get(k)))
                    {
                        rowGood = false;
                        break inner;
                    }
                    }
                }
                
                for(int k = 0; k < addingShipCols.size(); k++)
                {
                    inner:
                    {
                    if(currShip.getShipCols().contains(addingShipCols.get(k)))
                    {
                        colGood = false;
                        break inner;
                    }
                    }
                }
            }
        }
        else
        {
            ArrayList<Integer> addingShipRows = new ArrayList<Integer>();
            ArrayList<Integer> addingShipCols = new ArrayList<Integer>();
            addingShipCols.add(currCol);
            for(int i = 0; i < addingShipSize; i++)
            {
                addingShipRows.add(currRow + i);
            }
            
            for(int j = 0; j < totalShips; j++)
            {
                Ship currShip = allShips.get(j);
                for(int k = 0; k < addingShipRows.size(); k++)
                {
                    inner:
                    {
                    if(currShip.getShipRows().contains(addingShipRows.get(k)))
                    {
                        rowGood = false;
                        break inner;
                    }
                    }
                }
                
                for(int k = 0; k < addingShipCols.size(); k++)
                {
                    inner:
                    {
                    if(currShip.getShipCols().contains(addingShipCols.get(k)))
                    {
                        colGood = false;
                        break inner;
                    }
                    }
                }
            }
            
            
        }
        
        if(rowGood == false && colGood == false)
        {
            return false;
        }
        else
        {
            return true;
        }    
        
     }
    
}
