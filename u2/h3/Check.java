import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Check {
    static final String regex_request = "\\[\\d+.\\d+\\](\\d+)-FROM-(\\w)-(\\d+)-TO-(\\w)-(\\d+)";
    static final String regex_io = "\\[\\s*(\\d+.\\d+)\\](IN|OUT)-(\\d+)-(\\w)-(\\d+)-(\\d+)";
    static final String regex_emv = "\\[\\s*(\\d+.\\d+)\\](ARRIVE|OPEN|CLOSE)-(\\w)-(\\d+)-(\\d+)";
    static final String regex_f = "ADD-floor-(\\d+)-(\\d+)-(\\d+)-(\\d+.\\d+)-(\\d+)";
    static final String regex_b = "ADD-building-(\\d+)-(\\w)-(\\d+)-(\\d+.\\d+)";
    public static void main(String[] args) {
        HashMap<Integer, Info> infos = new HashMap<>();
        HashMap<Integer, Elevator> elevators = new HashMap<>();
        HashMap<Integer, Info> out = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        Pattern pattern = Pattern.compile(regex_request);
        Pattern pattern2 = Pattern.compile(regex_f);
        Pattern pattern3 = Pattern.compile(regex_b);
        boolean correct = true;
        for (int i = 0; i < 5; i++) {
            elevators.put(i+1,
                    new Elevator(i+1,1,String.valueOf('A'+i), 8, 0.6, 1<<(i)));
        }
        elevators.put(6,
                new Elevator(6, 1, "A", 8, 0.6, 31));
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.equals("end")) {
                break;
            }
            Matcher matcher = pattern.matcher(line);
            Matcher matcher2 = pattern2.matcher(line);
            Matcher matcher3 = pattern3.matcher(line);
            if (matcher.find()) {
                int id = Integer.parseInt(matcher.group(1));
                infos.put(id, new Info(line));
            } else if (matcher2.find()) {
                elevators.put(Integer.parseInt(matcher2.group(1)),
                        new Elevator(Integer.parseInt(matcher2.group(1)),
                        Integer.parseInt(matcher2.group(2)),
                        "A",
                        Integer.parseInt(matcher2.group(3)),
                        Double.parseDouble(matcher2.group(4)),
                        Integer.parseInt(matcher2.group(5))));
            } else if (matcher3.find()) {
                elevators.put(Integer.parseInt(matcher3.group(1)),
                        new Elevator(Integer.parseInt(matcher3.group(1)),
                                1,
                                matcher3.group(2),
                                Integer.parseInt(matcher3.group(3)),
                                Double.parseDouble(matcher3.group(4)),
                                1 << (matcher3.group(2).charAt(0) - 'A')));
            }
        }
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            Pattern pattern1 = Pattern.compile(regex_io);
            pattern2 = Pattern.compile(regex_emv);
            Matcher matcher1 = pattern1.matcher(line);
            Matcher matcher2 = pattern2.matcher(line);
            if (matcher1.find()) {//check matcher n!!!!!!
                int id = Integer.parseInt(matcher1.group(3));
                if (matcher1.group(2).equals("IN")) {
                    if (!out.containsKey(id)) {
                        out.put(id, new Info(matcher1.group(4), matcher1.group(5)));

                    } else {
                        if (!out.get(id).checkIO(matcher1.group(4), matcher1.group(5))) {
                            System.out.println("Passenger " + id + " enter the elevator in wrong place.");
                            correct = false;
                        }
                    }
                    elevators.get(Integer.parseInt(matcher1.group(6))).io("IN",
                            Double.parseDouble(matcher1.group(1)),
                            id);
                } else {
                    out.get(id).update(matcher1.group(4), matcher1.group(5));
                    elevators.get(Integer.parseInt(matcher1.group(6))).io("OUT",
                            Double.parseDouble(matcher1.group(1)),
                            id);
                }
            } else if (matcher2.find()) {
                elevators.get(Integer.parseInt(matcher2.group(5))).move(
                        Double.parseDouble(matcher2.group(1)),
                        matcher2.group(2),
                        matcher2.group(3),
                        Integer.parseInt(matcher2.group(4))
                );
            }
        }

        for (int i : infos.keySet()) {
            if (!infos.get(i).equals(out.get(i))) {
                correct = false;
                System.out.println("Passenger " + i + " hasn't arrive at his destination.");
            }
        }
        if (correct) {
            System.out.println("Congratulations! All passengers have arrived.");
        } else {
            System.out.println("You failed in this case. Please check your output");
        }
    }
}

class Info {
    String fb = "";
    String ff = "";
    String tb = "";
    String tf = "";
    public Info(String line) {
        Pattern pattern = Pattern.compile(Check.regex_request);
        Matcher matcher = pattern.matcher(line);
        matcher.find();
        fb = matcher.group(2);
        ff = matcher.group(3);
        tb = matcher.group(4);
        tf = matcher.group(5);
    }

    public void update(String tb, String tf) {
        this.tb = tb;
        this.tf = tf;
    }

    public Info(String fb, String ff) {
        this.fb = fb;
        this.ff = ff;
    }

    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Info) {
            Info t = (Info) obj;
            return fb.equals(t.fb) && tb.equals(t.tb) && ff.equals(t.ff) && tf.equals(t.tf);
        } else {
            return false;
        }
    }

    public boolean checkIO(String fb, String ff) {
        return fb.equals(tb) && ff.equals(tf);
    }
}

class Elevator {
    int id;
    int floor;
    String bd;
    double speed;
    int capacity;
    int carry;
    SwitchBit sb;
    ArrayList<Integer> passengers;
    double last;
    boolean running;

    public Elevator(int id, int floor, String bd, int capacity, double speed, int sb) {
        this.id = id;
        this.floor = floor;
        this.bd = bd;
        this.speed = speed;
        this.capacity = capacity;
        carry = 0;
        this.sb = new SwitchBit(sb);
        passengers = new ArrayList<>();
        last = -1;
        running = false;
    }

    public void io(String move, double time, int id) {
        if (time < last) {
            System.out.println("Time decline.");
        }
        last = time;
        if (move.equals("IN")) {
            passengers.add(id);
            carry += 1;
            if (carry > capacity) {
                System.out.println("Passenger " + id + " enter the elevator" + this.id +" while overload.");
            }
        } else {
            Iterator iterator = passengers.iterator();
            boolean correct = false;
            while (iterator.hasNext()) {
                Integer i = (Integer) iterator.next();
                if (i == id) {
                    iterator.remove();
                    correct = true;
                    carry -= 1;
                    break;
                }
            }
            if (!correct) {
                System.out.println("You create another Passenger " + id + " in elevator" + this.id +".");
            }
        }
    }

    public void move(double time, String move, String bd, int floor) {
        if (time < last) {
            System.out.println("Time decline!");
        }
        if (move.equals("OPEN")) {
            if (!sb.getByChar(bd.charAt(0))) {
                System.out.println("Elevator " + id + " opened in forbidden building at " + time + ".");
            }
            running = false;
        } else if (move.equals("ARRIVE")) {
            if (!running) {
                running = true;
            } else {
                if (time - last < speed - 0.05) {
                    System.out.println("Elevator " + id + " run too fast at " + time + ".");
                }
            }
        }
        last = time;
    }
}

class SwitchBit extends BitSet {
    public SwitchBit(int switchInfo) {
        super(5);
        int n = switchInfo;
        for (int i = 0; i < 5; i++) {
            if ((n & 1) == 1) {
                set(i);
            }
            n /= 2;
        }
    }

    public boolean getByChar(Character character) {
        return get(character - 'A');
    }

    public void setByChar(Character character) {
        set(character - 'A');
    }

    public boolean checkAccess4Char(Character current, Character destination) {
        return getByChar(current) && getByChar(destination);
    }

    @Override
    public String toString() {
        String s = "";
        for (int i = 0; i < 5; i++) {
            if (get(i)) {
                s += String.valueOf('A' + i);
            }
        }
        return s;
    }

    public boolean isImplicated(SwitchBit switchBit) {
        int count = 0;
        for (int i = 0; i < 5; i++) {
            if (get(i)) {
                if (!switchBit.get(i)) {
                    count += 1;
                    break;
                }
            }
        }
        for (int i = 0; i < 5; i++) {
            if (switchBit.get(i)) {
                if (!get(i)) {
                    count += 1;
                    break;
                }
            }
        }
        if (count == 2) {
            return false;
        }
        return true;
    }
}
