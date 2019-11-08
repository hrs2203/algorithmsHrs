import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.*;

class cal_date {
    int date;
    int month;
    int year;

    Random rand = new Random();

    cal_date() {
        // generate random date
        this.date = rand.nextInt(30) + 1;
        this.month = rand.nextInt(11) + 1;
        this.year = rand.nextInt(40) + 1980;
    }

    cal_date(int d, int m, int y) {
        this.date = d;
        this.month = m;
        this.year = y;
    }

    void setCalDateToToday() {
        this.date = 4;
        this.month = 11;
        this.year = 2019;
    }

    public void printDate() {
        System.out.println(this.date + "/" + this.month + "/" + this.year);
    }

    public String getDate() {
        return (this.date + "/" + this.month + "/" + this.year).toString();
    }

    public static int getDiff(cal_date a, cal_date b) {
        // b - a
        int temp_a = 365 * (a.year - 2010) + 30 * a.month + a.date;
        int temp_b = 365 * (b.year - 2010) + 30 * b.month + b.date;
        return Math.abs(temp_b - temp_a);
    }
}


class readHtmlFile {
    public static String ReadFile(String fileName) throws Exception {
        StringBuilder fileData = new StringBuilder();
        File htmlFile = new File(fileName);

        Scanner input = new Scanner(htmlFile);
        while (input.hasNextLine()) {
            fileData.append(input.nextLine());
        }
        input.close();

        return fileData.toString();
    }

    public static ArrayList<String> getQuestionList(String inputData) {

        // fetching the start point of quesiton block
        Pattern pattern = Pattern.compile("class=\"question-summary\"");
        Matcher StartSearch = pattern.matcher(inputData);

        ArrayList<Integer> startPointIndex = new ArrayList<>();
        while (StartSearch.find()) {
            startPointIndex.add(StartSearch.start());
        }

        // fetching the end point of quesiton block
        pattern = Pattern.compile("</div>[ ]*</div>[ ]*</div>[ ]*</div>[ ]*</div>[ ]*</div>");
        Matcher EndSearch = pattern.matcher(inputData);

        ArrayList<Integer> endPointIndex = new ArrayList<>();
        while (EndSearch.find()) {
            endPointIndex.add(EndSearch.end());
        }

        // storing in array so that each bolck can be processed individually
        ArrayList<String> questionBlocks = new ArrayList<String>();

        for (int i = 0; i < startPointIndex.size(); i++) {
            String data = inputData.substring(startPointIndex.get(i), endPointIndex.get(i));
            data = data.replaceAll(",", "");
            questionBlocks.add(data);
        }

        return questionBlocks;
    }

    public static int readVotes(String questionString) {
        Pattern StartSpan = Pattern.compile("<span class=\"vote-count-post \"><strong>");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);
        SpanOpenIndex.find();

        Pattern EndSpan = Pattern.compile("</strong></span>");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);
        SpanCloseIndex.find();

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());

        int votesCount = Integer.valueOf(valueStr);

        return votesCount;
    }

    public static int readAnswerCount(String questionString) {
        Pattern StartAnswerCountDiv = Pattern.compile("<div class=\"status answered\">[ ]*<strong>");
        Matcher AnswerCountOpenIndex = StartAnswerCountDiv.matcher(questionString);

        if (!AnswerCountOpenIndex.find())
            StartAnswerCountDiv = Pattern.compile("<div class=\"status answered-accepted\">[ ]*<strong>");
        AnswerCountOpenIndex = StartAnswerCountDiv.matcher(questionString);
        if (!AnswerCountOpenIndex.find())
            StartAnswerCountDiv = Pattern.compile("<div class=\"status unanswered\">[ ]*<strong>");
        AnswerCountOpenIndex = StartAnswerCountDiv.matcher(questionString);
        AnswerCountOpenIndex.find();

        Pattern EndAnswerCountDiv = Pattern.compile("</strong>answer[s ][ ]*</div>");
        Matcher AnswerCountCloseIndex = EndAnswerCountDiv.matcher(questionString);
        AnswerCountCloseIndex.find();

        String valueStr = questionString.substring(AnswerCountOpenIndex.end(), AnswerCountCloseIndex.start());
        int answerCount = Integer.valueOf(valueStr);

        return answerCount;
    }

    public static int readViews(String questionString) {
        Pattern StartSpan = Pattern.compile("<div class=\"views \" title=\"[,0-9]* views\">");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);
        if (!SpanOpenIndex.find()) {
            StartSpan = Pattern.compile("<div class=\"views warm\" title=\"[,0-9]* views\">");
            SpanOpenIndex = StartSpan.matcher(questionString);
            if (!SpanOpenIndex.find()) {
                StartSpan = Pattern.compile("<div class=\"views hot\" title=\"[,0-9]* views\">");
                SpanOpenIndex = StartSpan.matcher(questionString);
                SpanOpenIndex.find();
            }
        }

        Pattern EndSpan = Pattern.compile("views[ ]*</div>");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);
        SpanCloseIndex.find();

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());
        valueStr = valueStr.replaceAll("\\s", "");
        valueStr = valueStr.replace("k", "000");
        int votesCount = Integer.valueOf(valueStr);

        return votesCount;
    }

    public static String readQuestion(String questionString) {
        Pattern StartSpan = Pattern.compile("class=\"question-hyperlink\">");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);
        SpanOpenIndex.find();

        Pattern EndSpan = Pattern.compile("</a>[ ]*</h3>");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);
        SpanCloseIndex.find();

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());

        return valueStr;
    }

    public static String readQuestionLink(String questionString) {
        Pattern StartSpan = Pattern.compile("<h3>[ ]*<a href=\"");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);
        SpanOpenIndex.find();

        Pattern EndSpan = Pattern.compile("class=\"question-hyperlink\">");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);
        SpanCloseIndex.find();

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());

        return valueStr;
    }

    public static String UserLink(String questionString) {
        Pattern StartSpan = Pattern.compile("<div class=\"user-details\">[ ]*<a href=\"");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);

        Pattern EndSpan = Pattern.compile("\">[- a-zA-Z0-9]*</a>[ ]*<div class=\"-flair\">");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);

        if (!SpanOpenIndex.find() || !SpanCloseIndex.find()) {
            return "";
        }

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());

        return valueStr;
    }

    public static int UserID(String questionString) {
        Pattern StartSpan = Pattern.compile("<div class=\"user-details\">[ ]*<a href=\"");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);

        Pattern EndSpan = Pattern.compile("\">[- a-zA-Z0-9]*</a>[ ]*<div class=\"-flair\">");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);

        if (!SpanOpenIndex.find() || !SpanCloseIndex.find()) {
            return 1234;
        }

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());

        return Integer.valueOf(valueStr.split("/")[2]);
    }

    public static String UserName(String questionString) {
        Pattern StartSpan = Pattern.compile("<div class=\"user-details\">[ ]*<a href=\"");
        Matcher SpanOpenIndex = StartSpan.matcher(questionString);

        Pattern EndSpan = Pattern.compile("\">[- a-zA-Z0-9]*</a>[ ]*<div class=\"-flair\">");
        Matcher SpanCloseIndex = EndSpan.matcher(questionString);

        if (!SpanOpenIndex.find() || !SpanCloseIndex.find()) {
            return "1234";
        }

        String valueStr = questionString.substring(SpanOpenIndex.end(), SpanCloseIndex.start());

        return valueStr.split("/")[3];
    }

    public static ArrayList<String> tagName(String questionString) {
        ArrayList<String> tagList = new ArrayList<String>();
        String[] arr = questionString.split("<a[ ]*href=\"/questions/tagged/");
        for (int i = 1; i < arr.length; i++) {
            tagList.add(arr[i].split("\"[ ]*class=\"post-tag\"")[0]);
        }
        return tagList;
    }

    public static ArrayList<Integer> badgeList(String questionString) {
        String[] arr = questionString.split("class=\"badgecount\">");
        ArrayList<Integer> badgesCount = new ArrayList<Integer>();
        for (int i = 1; i < arr.length; i++) {
            String[] ar = arr[i].split("</span>[ ]*</span>");
            badgesCount.add(Integer.valueOf(ar[0]));
        }
        return badgesCount;
    }

    public static String publishDateTime(String questionString) {
        String[] arr = questionString.split("class=\"relativetime\">");
        String[] ar = arr[1].split("</span>[ ]*</div>");
        return ar[0];
    }
}

class Tag {
    String tagName;
    String tagLink;

    ArrayList<UserProfileSO> userList = new ArrayList<UserProfileSO>();
    ArrayList<StackOverflow> questionList = new ArrayList<StackOverflow>();

    Tag(String tgn) {
        this.tagName = tgn;
        this.tagLink = "stackoverflow.com/questions/tagged/" + tgn;
    }

    static boolean findTag(ArrayList<Tag> tagList , String tag_name){
        for (int i = 0; i < tagList.size(); i++) {
            if ( tag_name.equals(tagList.get(i).tagName) ){
                return true;
            }
        }
        return false;
    }

    void addNewUser(UserProfileSO newUser){
        this.userList.add(newUser);
    }

    void addNewQuesiton(StackOverflow newQuestion){
        this.questionList.add(newQuestion);
    }

}

class UserProfileSO{
    String userName;
    String LinkToUserProfile;
    int UserID;
    int goldBadgeCount;
    int silverBadgeCount;
    int bronzeBadgeCount;

    void setBadge(int b) {
        this.goldBadgeCount = 0;
        this.silverBadgeCount = 0;
        this.bronzeBadgeCount = b;
    }

    void setBadge(int s, int b) {
        this.goldBadgeCount = 0;
        this.silverBadgeCount = s;
        this.bronzeBadgeCount = b;
    }

    void setBadge(int g, int s, int b) {
        this.goldBadgeCount = g;
        this.silverBadgeCount = s;
        this.bronzeBadgeCount = b;
    }

    UserProfileSO(String user_name, String user_link, int uid, int[] badges) {
        this.userName = user_name;
        this.LinkToUserProfile = user_link;
        this.UserID = uid;
        if (badges.length == 3) {
            this.setBadge(badges[0], badges[1], badges[2]);
        } else if (badges.length == 2) {
            this.setBadge(badges[0], badges[1]);
        } else {
            this.setBadge(badges[0]);
        }
    }

    void showUserDetail(){
        System.out.println("UserName: "+this.userName);
        System.out.println("UserLink: "+this.LinkToUserProfile);
        System.out.println("User ID: "+this.UserID);
        System.out.println("Gold badges: "+this.goldBadgeCount);
        System.out.println("Silver badges: " + this.silverBadgeCount);
        System.out.println("Bronze badges: " + this.bronzeBadgeCount);
    }
    
}

class StackOverflow {
    String Question;
    String LinkToQuestion;
    Tag tags;
    int NoOfViews;
    int NoOfAnswer;
    UserProfileSO user;
    String postDate;
    String AnswerSnippet;

    StackOverflow(String question, String LTQ, int NOV, int NOA, String postdate, String ANS) {
        this.Question = question;
        this.LinkToQuestion = LTQ;
        // this.tags = tg; Tag tg,
        this.NoOfViews = NOV;
        this.NoOfAnswer = NOA;
        // this.user = u; UserProfileSO u,
        this.postDate = postdate;
        this.AnswerSnippet = ANS;
    }

}

public class Assign08064 {
    public static void main(String[] args) throws Exception {
        int val = 25145;
        for (int x = 0; x < 100; x++) {
            String start = "./sof-dataset/";
            String fileName = start + Integer.toString(val + x) + ".html";
            System.out.println(fileName + "\n----------------------------------------------------");
            String data = readHtmlFile.ReadFile(fileName);
            ArrayList<String> questionList = readHtmlFile.getQuestionList(data);
            for (int i = 0; i < questionList.size(); i++) {
                // System.out.println(questionList.get(i));
                System.out.println(i + 1 + " " + readHtmlFile.readVotes(questionList.get(i)) + " "
                        + readHtmlFile.readAnswerCount(questionList.get(i)) + " "
                        + readHtmlFile.readViews(questionList.get(i)) + " " + readHtmlFile.UserLink(questionList.get(i))
                        + " " + readHtmlFile.UserID(questionList.get(i)) + " "
                        + " " + readHtmlFile.UserName(questionList.get(i))
                        + " " + readHtmlFile.publishDateTime(questionList.get(i))
                );
                ArrayList<String> tags = readHtmlFile.tagName(questionList.get(i));
                for (int j = 0; j < tags.size(); j++) {
                    System.out.print(tags.get(j) + " ");
                }
                System.out.println("");
                // link for tag = /questions/tagged/<tagname>
                System.out.println(readHtmlFile.readQuestion(questionList.get(i)) + "\n"
                        + readHtmlFile.readQuestionLink(questionList.get(i)));
                ArrayList<Integer> bcount = readHtmlFile.badgeList(questionList.get(i));
                for (int j = 0; j < bcount.size(); j++) {
                    System.out.print(bcount.get(j) + " ");
                }
                System.out.println("\n");
            }
        }
    }
}