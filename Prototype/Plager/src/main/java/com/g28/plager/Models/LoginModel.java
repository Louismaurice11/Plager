package com.g28.plager.Models;


import com.g28.plager.SQL.Connector;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * The login model contains the users name and password, and will be
 * responsible for determining whether the user should be granted access to
 * the plagiarism algorithm.
 *
 * @author Xavier Parnell (psyxp1)
 */
public class LoginModel
{
	private String m_Username;
	private String m_Password;

	/**
	 * Set the users name
	 * @param username the name of the user to be set
	 */
	public void setUsername(String username){
		this.m_Username = username;
	}

	/**
	 * Set the users password
	 * @param username the password inputted by the user
	 */
	public void setPassword(String username){
		this.m_Password = username;
	}

	/**
	 * Query the MySQL server to attempt to match a username and password.
	 */
	public boolean authenticator() throws SQLException, ClassNotFoundException {
		//Instantiate connection manager
		Connector cM = new Connector();
		//Setup the connection to localhost MySQL server
		Connection connect =  cM.connection();

		//Create an SQL query to attempt to match username and password
		Statement statement = connect.createStatement();
		ResultSet rs = statement.executeQuery(
				"SELECT count(1) FROM `entries` WHERE `username` ='" +
						m_Username+"' AND `password` ='" + m_Password + "'");

		try{
			//While there are query results to be read...
			while(rs.next()){
				//Check if we find a unique login reference
				if(rs.getInt(1) == 1)
				{
					//Login success
					return true;
				}

			}

		}
		catch(Exception e){
			e.printStackTrace();
		}
		return false;
	}


}
