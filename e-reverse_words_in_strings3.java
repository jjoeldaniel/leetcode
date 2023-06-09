class Solution {
    public String reverseWords(String s) {
        
        List<String> list = new ArrayList<String>(Arrays.asList(s.split(" ")));
        int wordCount = list.size();
        String message = "";
        
        // Checks each word
        for (int i = 0; i < wordCount; ++i) {
            
            // Selects word
            String word = list.get(i);
            int bound_index = (word.length() - 1);
            
            // Reverses word
            String[] backwards = word.split("");
            for (int x = bound_index + 1; x > 0; --x) {
                message += backwards[x-1];
            }
            message += " ";
        }
        message = message.substring(0, message.length()-1);
       return message;
    }
}