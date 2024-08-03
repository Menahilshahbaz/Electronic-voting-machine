from tkinter import messagebox, simpledialog

class Candidate:
    def __init__(self, name, cnic, cand_pswd):
        self.name = name
        self.cnic = cnic
        self.cand_pswd = cand_pswd
        self.votes = 0

class Voter:
    def __init__(self, name, cnic):
        self.name = name
        self.cnic = cnic
        self.status = False
        self.voted_for = None

class VotingMachine:
    def __init__(self):
        self.candidates = {} 
        self.voters = {}
        self.num_voters = 0

    def add_candidate(self, name, cnic, cand_pswd):
        self.candidates[cnic] = Candidate(name, cnic, cand_pswd)
    
    def add_voter(self, name, cnic):
        self.voters[cnic] = Voter(name, cnic)

    def admin_login(self, username, password):
        if username == "admin" and password == "123":
            return True
        return False
    
    def candidate_login(self, cnic, password):
            if cnic in self.candidates and password in self.candidates[cnic].cand_pswd:
                return True
            return False

    def voter_login(self, cnic):
            for name in self.candidates:
                if cnic in self.candidates[name].cnic:
                    return False
            return True

    def view_details(self):
        details = f"\nEnrolled Candidates: {len(self.candidates)}\n"
        for cnic, candidate in self.candidates.items():
            details += f"{candidate.name} : \n CNIC = {cnic} : \n Password = {candidate.cand_pswd} : \n Votes =  {candidate.votes}\n\n"
        
        details += f"\nNumber of Voters are: {len(self.voters)}\n"
        for cnic, voter in self.voters.items():
            details += f"{voter.name} with CNIC : {cnic}"
        
        messagebox.showinfo("Complete Details", details)

    def candidate_results(self, cnic):
        details = "\nResults:\n"
        for c_cnic, candidate in self.candidates.items():
            if c_cnic == cnic:
                details += f"{candidate.name}: {candidate.votes} votes\n"
        details += f"Total number of voters: {self.num_voters}\n"
        messagebox.showinfo("Your Result", details)
    
    def view_results(self):
        details = f"\nResults:\n"
        for cnic, candidate in self.candidates.items():
            details = f"{candidate.name}: {candidate.votes} votes\n"
        details = f"Total number of Candidates: {len(self.candidates)}\n"  
        details = f"Total number of voters: {self.num_voters}\n"
        messagebox.showinfo("Voting Results", details)

    def change_driver_password(self, cnic, old_pswd, new_pswd, confirm_pswd):
        if old_pswd == self.candidates[cnic].cand_pswd:
            if new_pswd == confirm_pswd:
                self.candidates[cnic].cand_pswd = new_pswd
                messagebox.showinfo("Success", "Password changed successfully!")
            else:
                messagebox.showerror("Error", "New Password didn't match!")
        else:
            messagebox.showerror("Error", "Old Password is Incorrect!")

    def voter_functions(self, v_cnic):
        print(v_cnic)
        if self.voters[v_cnic].status == False:
            text = "Candidates:\n"
            for cnic, candidate in vm.candidates.items():
                text += f"{candidate.name}\n"
            vote_for = simpledialog.askstring("Chose Candidate", text)
            print(v_cnic)
            vm.vote(vote_for, v_cnic)
            
        else:
            text = f"You have already voted: {self.voters[v_cnic].voted_for}\n"
            messagebox.showerror("Error", text)

    def check_vote_for(self, name):
        for cnic in self.candidates:
            if name == self.candidates[cnic].name:
                return True
        return False

    def vote(self, vote_for, v_cnic):
        if vm.check_vote_for(vote_for):
            for cnic in self.candidates:
                if vote_for == self.candidates[cnic].name:
                    self.candidates[cnic].votes += 1
                    self.num_voters += 1
                    self.voters[v_cnic].status = True
                    self.voters[v_cnic].voted_for = vote_for
                    text = f"You Successfully Voted for {self.candidates[cnic].name}!"
                    messagebox.showinfo("Success", text)
        else:
            messagebox.showerror("Error", "Invalid Selection!")   


    def valid_candidate(self, cnic):
        for name in vm.candidates:
            if cnic in self.candidates[name].cnic:
                return False
        for name in vm.voters:
            if cnic in self.voters:
                return False
        return True

    def nota_voter(self, cnic):
        for name in vm.voters:
            if cnic in self.voters:
                return False
        return True

vm = VotingMachine()
vm.add_candidate("Ali", "111", "123")
vm.add_candidate("Hassan", "222", "123")  