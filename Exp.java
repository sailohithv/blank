package sample;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Exp {

	public static void main(String[] args) throws IOException {

		String targetTablle = "target"; // TARGET TABLE

		List<String> sourceTables = new ArrayList<String>(); // SOURCE TABLES
		sourceTables.add("sdf");
		sourceTables.add("sdfsdfsad");
		sourceTables.add("asdasdfasdfasdf");
		sourceTables.add("asdaasdfasdfadfsdfasdfasdf");
		List<ArrayList<String>> coulumsgsd = new ArrayList<ArrayList<String>>();
		ArrayList<String> temp = new ArrayList<String>();
		temp.add("table1column"); // COLUMNS FOR TABLE 1
		temp.add("table1column1");
		temp.add("table1column2");
		coulumsgsd.add(temp);

		temp = new ArrayList<String>(); // COLUMNS FOR TABLE 2
		temp.add("table2column");
		temp.add("table2column1");
		temp.add("table2column2");
		coulumsgsd.add(temp);

		temp = new ArrayList<String>(); //// COLUMNS FOR TABLE 3
		temp.add("table3column");
		temp.add("table3column1");
		temp.add("table3column2");
		coulumsgsd.add(temp);
		temp = new ArrayList<String>();
		temp.add("table4column"); // COLUMNS FOR TABLE 1
		temp.add("table4column1");
		temp.add("table4column2");
		temp.add("table4column3");
		coulumsgsd.add(temp);
		
		
		File f = new File("C:\\Users\\LOHITH\\Desktop\\New folder\\fk.html");		//File creation
		FileWriter fos = new FileWriter(f);									
		StringBuffer sb = new StringBuffer();
		sb.append("<html><head>");
		sb.append(
				"<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css\">");
		sb.append("<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>");
		sb.append(" <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js\"></script>");
		sb.append("</head><body>");
		sb.append("<div class=\"container\">");
		sb.append("<center>");
		sb.append("<br/>");
		sb.append("<br/>");
		sb.append("<br/>");
		sb.append("<table  class=\"table table-hover\" style=\"text-align:center; \"><tr >");
		sb.append("<td");
		sb.append(" rowspan=\"");
		sb.append(sourceTables.size() );
		sb.append("\"");
		sb.append(" style=\"font-size:40px; color:red;width:30% ; text-align:center; vertical-align : middle ;\"");
		
		sb.append(">");
		sb.append(targetTablle);
		sb.append("</td><td>");
		for (int i = 0; i < sourceTables.size(); i++) {
			
			sb.append(
					"<table class=\"table table-striped\" style=\"border:2px solid black; text-align:center; \"><tr>");
			sb.append("<td ");
			sb.append("rowspan=\"");
			sb.append(coulumsgsd.get(i).size() + 1);

			sb.append("\" style=\"vertical-align : middle;width : 30% \">");
			sb.append(sourceTables.get(i));

			for (String str : coulumsgsd.get(i)) {
				sb.append("<tr >");
				sb.append("<td style=\"border:2px solid black; text-align:center; \">");
				sb.append(str);
				sb.append("</td></tr>");

			}
			sb.append("</table>");
			sb.append("<br/>");
			sb.append("</center>");
		}
		sb.append("</td>");
		sb.append("<tfoot><tr><td colspan=\"2\"> ");
		//sb.append("<---------------------------------------------------------------------------------------------------------------------------");
		for(int l=0;l<50;l++)
		sb.append("<span class=\"glyphicon glyphicon-arrow-left\"></span>");
		
		sb.append("</td></tr></tfoot>");
		sb.append("</table></div>");

		sb.append("</body></html>");

		fos.write(sb.toString());
		// TODO Auto-generated method stub
		fos.close();
	}
}
