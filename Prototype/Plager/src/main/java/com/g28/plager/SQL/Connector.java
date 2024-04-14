package com.g28.plager.SQL;
import java.sql.*;

/**
 * The class used to query the MySQL database for the prototype of the
 * project. Will be used to implement a basic login system for demonstration
 * purposes.
 *
 * @author Xavier Parnell (psyxp1)
 */
public class Connector {
	public Connection connection;
	public Connection connection() throws ClassNotFoundException,
			SQLException {

		String url = "jdbc:mysql://localhost:3308/PrototypeDB";
		//Create the connection
		Class.forName("com.mysql.cj.jdbc.Driver");
		connection = DriverManager.getConnection(url
				,"userAdmin","group28");

		return connection;
	}
}
