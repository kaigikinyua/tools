import System.IO;

class Advanced{
	public static void main(String,args[]){

	}
}

class Student{
	public static boolean addStudent(String studentname,String password,String regNum){}
	public static boolean logInStudent(String regNum, String password){}

}

class Lessons{
	public static List<String> getAvalableLessons(){}
	public static boolean addLesson(String lessonName,String lessonID){}
	public static boolean deleteLesson(String lessonID){}
}

class Teachers{
	public static List<String> getTeachers(){}
	public static boolean deleteTeacher(String teacherID){}
	public static boolean addTeacher(String teacherID,String name){}
	public static boolean allocateTeacher(String teacherID,String lessonID){}
}