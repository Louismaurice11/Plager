package com.g28.plager;

import java.net.URL;

import com.g28.plager.Controllers.LoginController;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;

/**
 * The main application which calls on the parser and detection algorithm
 *
 * @author Conor Cowley (psycc4)
 * @author Xavier Parnell (psyxp1)
 */
public class PlagerApp extends Application
{
    @Override
    public void start(Stage stage) throws Exception
    {

        // Retrieve the view
        URL location = getClass().getClassLoader().getResource("Views" +
                "/Login.fxml");

        // Load the view
        FXMLLoader loader = new FXMLLoader(location);

        // Initialise the scene
        Scene scene = new Scene(loader.load(), 600, 400);

        // Retrieving the controller fetched by the FXMLoader
        LoginController controller = loader.getController();

        // Setting the stage the login screen will run on
        controller.setStage(stage);

        // Setting the window icon to the Plager logo
        stage.getIcons().add(new Image("/images/logoBright.png"));
        // Setting the stage to not be resizable
        stage.setResizable(false);
        // Setting the title of the stage
        stage.setTitle("Plager");
        // Setting the scene and showing the screen
        stage.setScene(scene);
        stage.show();

    }

}