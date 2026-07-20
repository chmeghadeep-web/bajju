import java.util.*;

class CommitNode {
    int commitId;
    String message;
    ArrayList<String> files;
    CommitNode next;

    CommitNode(int id, String msg, ArrayList<String> files) {
        this.commitId = id;
        this.message = msg;
        this.files = new ArrayList<>(files); // Copy staged files
        this.next = null;
    }
}

class Git {

    private CommitNode head;
    private ArrayList<String> stagingArea;
    private int commitCounter;

    public Git() {
        head = null;
        stagingArea = new ArrayList<>();
        commitCounter = 1;
    }

    
    public void gitAdd(String file) {

        if (!stagingArea.contains(file)) {
            stagingArea.add(file);
            System.out.println(file + " added to staging area.");
        } else {
            System.out.println(file + " already exists in staging area.");
        }
    }

    
    public void gitRm(String file) {

        if (stagingArea.remove(file)) {
            System.out.println(file + " removed from staging area.");
        } else {
            System.out.println(file + " not found in staging area.");
        }
    }

    
    public int gitCommit(String msg) {

        if (stagingArea.isEmpty()) {
            System.out.println("Nothing to commit.");
            return -1;
        }

        CommitNode newNode =
                new CommitNode(commitCounter, msg, stagingArea);

        if (head == null) {
            head = newNode;
        } else {
            CommitNode temp = head;

            while (temp.next != null) {
                temp = temp.next;
            }

            temp.next = newNode;
        }

        stagingArea.clear();

        System.out.println("Commit Successful.");

        return commitCounter++;
    }

    
    public void gitAmend(int cid, String newMsg) {

        CommitNode temp = head;

        while (temp != null) {

            if (temp.commitId == cid) {

                if (temp.next != null) {
                    System.out.println("Cannot amend older commits.");
                    return;
                }

                temp.message = newMsg;
                System.out.println("Commit amended successfully.");
                return;
            }

            temp = temp.next;
        }

        System.out.println("Commit ID not found.");
    }

    
    public void gitCheckout(int cid) {

        CommitNode temp = head;

        while (temp != null) {

            if (temp.commitId == cid) {

                temp.next = null;
                System.out.println("Checked out to Commit " + cid);
                return;
            }

            temp = temp.next;
        }

        System.out.println("Commit not found.");
    }

    
    public void gitLog() {

        if (head == null) {
            System.out.println("No commits available.");
            return;
        }

        CommitNode temp = head;

        System.out.println("\n========= GIT LOG =========");

        while (temp != null) {

            System.out.println("----------------------------");
            System.out.println("Commit ID : " + temp.commitId);
            System.out.println("Message   : " + temp.message);

            System.out.print("Files     : ");

            for (String file : temp.files) {
                System.out.print(file + " ");
            }

            System.out.println();

            temp = temp.next;
        }

        System.out.println("----------------------------");
    }
}

public class GitOperations {

    public static void main(String[] args) {

        Git git = new Git();

        
        git.gitAdd("Main.java");
        git.gitAdd("Login.java");

        
        int id1 = git.gitCommit("Initial Commit");

        git.gitAdd("Home.java");
        git.gitAdd("Dashboard.java");

        int id2 = git.gitCommit("Added Home and Dashboard");

        git.gitAdd("Profile.java");

        
        int id3 = git.gitCommit("Added Profile Page");

        
        git.gitLog();

        git.gitAmend(id3, "Updated Profile Page");

        System.out.println("\nAfter Amend:");

        git.gitLog();

        git.gitCheckout(id2);

        System.out.println("\nAfter Checkout:");

        git.gitLog();
    }
}