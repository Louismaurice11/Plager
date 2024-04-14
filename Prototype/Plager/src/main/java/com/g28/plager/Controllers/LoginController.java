package com.g28.plager.Controllers;

import com.g28.plager.Models.LoginModel;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Button;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.image.ImageView;
import javafx.scene.text.Text;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.URL;
import java.sql.SQLException;

/**
 * The login screen of the prototype, where the user can input their username
 * and password in order to access the application functionality.
 *
 * @author Xavier Parnell (psyxp1)
 */
public class LoginController {
	@FXML private Button m_ExitButton;
	@FXML
	private PasswordField m_UserPasswordField;
	@FXML
	private TextField m_UsernameField;
	@FXML
	private Text m_IncorrectText;
	@FXML
	private Button m_LoginButton;
	private Stage m_Stage;
	private LoginModel m_LoginModel;

	public void setStage(Stage stage) {
		this.m_Stage = stage;
	}
	private Stage getStage(){
		return this.m_Stage;
	}

	/**
	 * <p>Method invoked upon m_LoginButton being clicked by the user.
	 * Checks the model for password and username matches, and shows the
	 * main application view if true.</p>
	 * @param actionEvent the actionEvent from the calling Object
	 */
	public void showMainView(ActionEvent actionEvent) throws IOException, SQLException, ClassNotFoundException {
		//Instantiate the model
		this.m_LoginModel = new LoginModel();

		//Null check inputted strings for username and password
		if(this.m_UsernameField.getText().isEmpty() ||
				this.m_UserPasswordField.getText().isEmpty() ){
			this.m_IncorrectText.setVisible(true);
			return;
		}
		//Set the input fields in the model
		this.m_LoginModel.setUsername(this.m_UsernameField.getText());
		this.m_LoginModel.setPassword(this.m_UserPasswordField.getText());

		//Determine a match in the model
		if(this.m_LoginModel.authenticator()){
			//Obtain the main view FXML file
			URL location = getClass().getClassLoader().getResource("Views/Main" +
						".fxml");
			// Load the view
			FXMLLoader loader = new FXMLLoader(location);
			//Set the new view
			this.m_Stage.getScene().setRoot(loader.load());
		}
		else{
			//No match found show retry message to user
			this.m_IncorrectText.setVisible(true);
		}

	}

	public void showMainViewWithoutLogin(ActionEvent actionEvent) throws IOException,	SQLException, ClassNotFoundException {
		//Instantiate the model
		this.m_LoginModel = new LoginModel();

		//Null check inputted strings for username and password
		if(this.m_UsernameField.getText().isEmpty() ||
				this.m_UserPasswordField.getText().isEmpty() ){
			this.m_IncorrectText.setVisible(true);
			return;
		}
		//Obtain the main view FXML file
		URL location = getClass().getClassLoader().getResource("Views/Main" +
				".fxml");
		// Load the view
		FXMLLoader loader = new FXMLLoader(location);
		//Set the new view
		this.m_Stage.getScene().setRoot(loader.load());


	}

	/**
	 * The method invoked upon the exit button clicked, to close the
	 * application.
	 * @param actionEvent the actionEvent of the calling button
	 */
	public void closeApplication(ActionEvent actionEvent) {
		Platform.exit();
	}
}
