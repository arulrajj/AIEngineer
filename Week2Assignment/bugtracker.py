
class BugTracker:

    def __init__(self, bugs):
        self.bugs = bugs
        
    def add_bug(self, bug_id, description, severity):
        self.bugs[bug_id] = {"description":description, "severity":severity, "status": "open"}

    def update_status(self, bug_id, new_status):
        self.bugs[bug_id]["status"] = new_status

    def list_all_bugs(self):
        for bug_id, bug_dict in self.bugs.items():
            print(f"Bug Id: {bug_id}")
            for key, value in bug_dict.items():
                print(f"  {key}: {value}")

    

if __name__ == "__main__":
    bugs = {"bug_123": {"description":"cosmetic issue", "severity":"low", "status": "open"},
            "bug_124": {"description":"functional issue", "severity":"medium", "status": "in progress"},
            "bug_125": {"description":"Security issue", "severity":"high", "status": "closed"}}
    bugtracker = BugTracker(bugs)
    print("List of bugs before adding a new one:")
    bugtracker.list_all_bugs()
    bugtracker.add_bug("bug_126", "Non functional issue", "medium")
    print("\n")
    print("List of bugs after adding a new one:")
    bugtracker.list_all_bugs()
    bugtracker.update_status("bug_123", "closed")
    print("\n")
    print("List of bugs after updating the status of one of the defect:")
    bugtracker.list_all_bugs()