class Solution {
    public String interpret(String command) {
        StringBuilder ans = new StringBuilder("");
        for(int i=0 ; i<command.length() ; i++){
            if(command.charAt(i)=='G'){
                ans.append('G');
            }else if(command.charAt(i)=='(' && command.charAt(i+1)==')'){
                i++;
                ans.append('o');
            }else{
                i+=3;
                ans.append('a').append('l');
            }
        }
        return ans.toString();
    }
}