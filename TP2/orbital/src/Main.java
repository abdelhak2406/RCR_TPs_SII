import orbital.WordSet; 

public class Main {

    public static void main(String[] args) {

   // Initialisation des 3 Mondes
        // Monde W1
        WorldSet world1 = new WorldSet();
        world1.addFormula(a.e.NOT+"A");
        // Monde W2
        WorldSet world2 = new WorldSet();
        world2.addFormula("A");
        world2.addFormula(a.e.NOT+"B");
        // Monde W3
        WorldSet world3 = new WorldSet();
        world3.addFormula("A");
        world3.addFormula(a.e.NOT+"B"+a.e.AND+"C");
    }
}
