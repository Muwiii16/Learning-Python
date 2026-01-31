import java.util.Random;

public class Joke{
    public static void main(String[]args){

        String[] jokes = {
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't programmers like nature? It has too many bugs.",
            "Why do cows have hooves instead of feet? Because they lactose.",
            "Why did the bicycle fall over? Because it was two-tired!"
        };

        Random random = new Random();
        int index = random.nextInt(jokes.length);
        System.out.println(jokes[index]);

    }
}