class Student():
    def __init__(self, first_n, last_n, major, hours, gpa, id):
        self.__first_n = first_n
        self.__last_n = last_n
        self.__major = major
        self.__hours = hours
        self.__gpa = gpa
        self.__id = id
    
    def get_first_n(self):
        return self.__first_n
    def set_first_n(self, new_first):
        self.__first_n = new_first
    
    def get_last_n(self):
        return self.__last_n
    
    def get_major(self):
        return self.__major
    def set_major(self, new_major):
        self.__major = new_major

    def get_hours(self):
        return self.__hours
    def set_hours(self, new_hours):
        self.__hours = new_hours

    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa

    def get_id(self):
        return self.__id
    
    def get_class_level(self):
        if self.__hours < 31:
            return "Freshman"
        elif self.__hours < 61:
            return "Sophomore"
        elif self.__hours < 90:
            return "Junior"
        else:
            return "Senior"
        
    def update_credit_hours(hours, additional_hours):
        hours += additional_hours
        return hours
    
    def print_student_data(self):
        print(f"Name: {self.__first_n} {self.__last_n} \nMajor: {self.__major} \nHours: {self.__hours} \nGPA: {self.__gpa} \nID: {self.__id} \nClass: {self.get_class_level()}")