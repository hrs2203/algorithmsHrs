/**
 * Hrishabh Pandey
 * S20180010064
 */

import java.util.*;

class RandValGen {
    /**
     * Generates random Int
     * 
     * @param s : start
     * @param e : end
     * @return Int b\w [s,e] inclusive at both end
     */
    public static int getInt(int s, int e) {
        Random rand = new Random();
        return s + rand.nextInt(e);
    }
}

/**
 * Problem1
 */
class soluton1 {

    /**
     * prints 2X2 matrix
     * 
     * @param a : matric
     * @param i : [-][0] index
     * @param j : [0][-] index
     */
    void print2x2(int[][] a, int i, int j) {
        System.out.println(a[i][j] + " " + a[i][j + 1]);
        System.out.println(a[i + 1][j] + " " + a[i + 1][j + 1]);
        System.out.println(" ");
    }

    /**
     * prints all the 2x2 matrix following given property
     * 
     * @param mat : nXm matrix
     * @param n   : dimension
     * @param m   : dimension
     */
    void printMatrix(int[][] mat, int n, int m) {
        int count = 0; // total number of such matrix
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < m - 1; j++) {
                if (mat[i][j] + mat[i + 1][j + 1] == mat[i][j + 1] + mat[i + 1][j]) {
                    count++;
                    print2x2(mat, i, j);
                }
            }
        }
        System.out.println("Total number of such matrices is " + count);
    }

    /**
     * function that will run this problem
     */
    public void executeQ1() {
        int n = 9;
        int m = 10;
        int m0[] = { 2, 7, 5, 11, 7, 9, 2, 17, 9, 9 };
        int m1[] = { 4, 5, 9, 83, 59, 8, 1, 3, 5, 5 };
        int m2[] = { 6, 2, 6, 9, 5, 9, 7, 9, 23, 3 };
        int m3[] = { 3, 4, 8, 1, 11, 7, 5, 9, 4, 6 };
        int m4[] = { 1, 2, 6, 13, 8, 4, 5, 6, 89, 7 };
        int m5[] = { 8, 4, 2, 9, 3, 1, 6, 8, 41, 5 };
        int m6[] = { 3, 97, 7, 1, 4, 7, 3, 5, 2, 3 };
        int m7[] = { 5, 2, 5, 28, 20, 4, 9, 35, 5, 6 };
        int m8[] = { 7, 4, 3, 14, 6, 2, 7, 5, 5, 2 };
        int[][] matrix = { m0, m1, m2, m3, m4, m5, m6, m7, m8 };

        printMatrix(matrix, n, m);
    }

}

/**
 * storing deatil of city
 */
class City {
    int placeId;
    int Popular;
    // destinationId dist
    Map<Integer, Float> Distance = new HashMap<Integer, Float>();
    ArrayList<Integer> travels = new ArrayList<Integer>();
    // destinationId traveltime
    Map<Integer, Integer> time = new HashMap<Integer, Integer>();
    ArrayList<String> announcement = new ArrayList<String>();

    /**
     * general deatails of a city
     */
    City() {
        this.placeId = RandValGen.getInt(10000, 99999);
        this.Popular = RandValGen.getInt(1, 9);

        int travelCount = RandValGen.getInt(1, 50);
        while (travelCount > 0) {
            this.travels.add(travelCount);
            travelCount--;
        }
    }

    /**
     * make announcement
     * @param intId : popular id
     */
    void makeAnnouncement(int intId,String ann){
        if (this.Popular == intId){
            this.announcement.add(ann);
        }
    }

    /**
     * Saving connection b\w 2 cities
     * 
     * @param destId : Id of destination city
     * @param dist   : distance to destination [10.0,200.0]
     * @param t_time : travel time [60,720]
     */
    void createConnection(int destId, Float dist, Integer t_time) {
        this.Distance.put(destId, dist);
        this.time.put(destId, t_time);
    }

    /**
     * Prints each City detail
     */
    void printCityDeatil() {
        System.out.println("City Id : " + this.placeId);
        System.out.println("Popular : " + this.Popular);

        System.out.println("List of all travel Agencys : ");
        for (int i = 0; i < this.travels.size(); i++) {
            System.out.print(this.travels.get(i) + " ");
        }
        System.out.println(" ");

        System.out.println("Destination ID - Distance - Travel Time");
        for (Integer Did : this.Distance.keySet()) {
            System.out.println(Did + " - " + this.Distance.get(Did) + " - " + this.time.get(Did));
        }
        System.out.println("Announcement : ");
        for (int i = 0; i < this.announcement.size(); i++) {
            System.out.println(this.announcement.get(i));
        }
        System.out.println("\n\n");
    }

}

/**
 * connecting cities
 */
class RoadMap {
    // source , list of destinations from that source
    Map<Integer, ArrayList<Integer>> connection = new HashMap<Integer, ArrayList<Integer>>();

    /**
     * Creates connection and store it in the above hashMap
     * 
     * @param cityList : list of all available cities
     */
    RoadMap(ArrayList<City> cityList) {

        int cityCount = cityList.size();

        for (City city : cityList) {
            ArrayList<Integer> destIds = new ArrayList<Integer>();

            int count = RandValGen.getInt(3, 30);

            for (int i = 0; i < count; i++) {
                int randInd = RandValGen.getInt(0, cityCount - 1);

                if (cityList.get(randInd).placeId != city.placeId) {
                    destIds.add(cityList.get(randInd).placeId);

                    float dist = RandValGen.getInt(10, 190);
                    int t_time = RandValGen.getInt(60, 720);
                    cityList.get(randInd).createConnection(city.placeId, dist, t_time);
                    city.createConnection(cityList.get(randInd).placeId, dist, t_time);
                }
            }

            connection.put(city.placeId, destIds);
        }
    }

    /**
     * common attracions
     * @param city
     */
    void findCommonPopulatAttraction(ArrayList<City> city){
        int count = city.size();
        Map<Integer,ArrayList<Integer>> data = new HashMap<Integer, ArrayList<Integer>>();
        for (int i = 0; i < count; i++) {
            if ( data.containsKey(city.get(i).Popular) ){
                data.get(city.get(i).Popular).add( city.get(i).placeId );
            }else{
                ArrayList<Integer> t = new ArrayList<Integer>();
                t.add( city.get(i).placeId );
                data.put(city.get(i).Popular,t);
            }
        }
        for (Integer id : data.keySet()) {
            System.out.print("popular "+id+" : ");
            for (Integer d : data.get(id)) {
                System.out.print(d+" ");
            }
            System.out.println("\n\n");
        }

    }

}

/**
 * Problem2
 */
class soluton2 {

    /**
     * Executes solution of question 2
     */
    public void executeQ2() {
        ArrayList<City> allCity = new ArrayList<City>();

        // creating random city's and storing
        int cityCount = RandValGen.getInt(100, 200); // n in question paper
        for (int i = 0; i < cityCount; i++) {
            City temp = new City();
            // temp.printCityDeatil();
            allCity.add(temp);
        }

        // creating random connection's b\w city's
        RoadMap allConn = new RoadMap(allCity);

        // printing all details of city and there respective connections
        System.out.println("Detail of all created citys\n");
        for (int i = 0; i < cityCount; i++) {
            allCity.get(i).printCityDeatil();
        }

        // printing common popular spots
        System.out.println("List of all common popular point");
        System.out.println("Popular place ID : list of place Id of citys\n\n");
        allConn.findCommonPopulatAttraction(allCity);

        // generating announcement
        int count = RandValGen.getInt(1, 100);
        for (int i = 0; i < count; i++) {
            int id = RandValGen.getInt(0, cityCount);
            String an = "Special announcement "+id;
            for (int j = 0; j < cityCount; j++) {
                allCity.get(j).makeAnnouncement(id, an);
            }
        }
    }

}

/**
 * EndSem18064
 */
public class EndSem18064 {
    public static void main(String[] args) {
        soluton1 ans1 = new soluton1();
        System.out.println("Solution of problem 1");
        ans1.executeQ1();
        System.out.println("---------------------------------------------");
        soluton2 ans2 = new soluton2();
        System.out.println("Solution of problem 2");
        ans2.executeQ2();
    }
}