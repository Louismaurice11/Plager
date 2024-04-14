package com.g28.plager.Controllers;

import com.g28.plager.Antlr.PreProcessors.CPreProcessor;
import com.g28.plager.Antlr.PreProcessors.PreProcessor;
import com.g28.plager.Logic.Detector;
import com.g28.plager.Models.FileModel;
import com.g28.plager.Models.MenuModel;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Alert;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.text.Text;
import javafx.stage.FileChooser;
import javafx.stage.Stage;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.Array;
import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

/**
 * The main screen of the prototype, where the user can load two files
 * and see the code and their similarity measure
 *
 * @author Conor Cowley (psycc4)
 * @author Xavier Parnell (psyxp1)
 */
public class MainController implements Initializable
{
    @FXML private Text m_LoadingText;
    /**
     * The field containing all the original code
     */
    @FXML
    private TextArea m_SourceField;

    /**
     * The field containing the suspected plagiarised code
     */
    @FXML
    private TextArea m_PlagiarisedField;

    /**
     * The button responsible for allowing the user to load the
     * plagiarised code to the screen
     */
    @FXML
    private Button m_LoadPlagiarised;

    /**
     * The button that initiates the main algorithm and produces a
     * similarity measure for the user
     */
    @FXML
    private Button m_PlagerIt;

    /**
     * The button responsible for allowing the user to load the original
     * source code to the screen
     */
    @FXML
    private Button m_LoadSource;

    /**
     * The model which gives the controller access to the current files loaded,
     * providing preprocessing functionally to the controller
     */

    private final MenuModel m_Model = new MenuModel();

    /**
     * The model which allows the controller to store instances of the preprocessed files,
     * so the main algorithm has access to them
     */

    private final FileModel m_FModel = new FileModel();


    /**
     * An instance of the users desktop, so the user can use the OS's file
     * application to retrieve the file
     */
    private Desktop m_Desktop = Desktop.getDesktop();

    /**
     * Responsible for allowing the user to select files from their own file path
     * provides an interaction between the program and the OS
     */
    private final FileChooser m_FileChooser = new FileChooser();

    /**
     * Creating a reference of the detector to run the algorithm with
     *
     */
     private Detector m_Detector;

    /**
     * The stage the screen is running on
     */
    private Stage m_Stage;


    private List<String> m_CodeFragments;
    /**
     * The initialize method sets the main structure of the screen
     * @param url The location of the screen (an FXML file)
     * @param resourceBundle The resources, interpreted as a JavaFX resourceBundle object
     */
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle)
    {
        m_PlagiarisedField.setDisable(true);
        m_SourceField.setDisable(true);

    }

    /**
     * A utility method that loads the source code to the screen and also preprocesses it
     * @param actionEvent The event that activates the method i.e. a button press
     * @throws IOException An error is thrown if the file cannot be accessed
     */
    public void loadSourceCode(ActionEvent actionEvent) throws IOException
    {
        // Access the model and set the current file
        m_Model.setSourceFile(m_FileChooser.showOpenDialog(m_Stage));

        //  If the current file in the model isn't null
        if (m_Model.getSourceFile() != null)
        {
            // We can attempt to open the file
            openFile(m_Model.getSourceFile());
        }

        // We are then loading the text onto the main screen
        m_SourceField.setText(m_Model.getSourceText());

        // Retrieving the preprocessor from the model and initialising the parser
        m_Model.getProcessor().initParser(m_Model.getSourceFile());

        // The parser parses the text and then saves it to the preprocessed files resource
        m_Model.getProcessor().preProcessFile();

        // Gives the file model access to the preprocessed file
        m_FModel.setPreProcessedSource(m_Model.getProcessor().getPreProcessedFile());

    }

    /**
     * A utility method that loads the plagiarised code to the screen and also preprocesses it
     * @param actionEvent The event that activates the method i.e. a button press
     * @throws IOException An error is thrown if the file cannot be accessed
     */
    public void loadPlaigarisedCode(ActionEvent actionEvent) throws IOException
    {

        // Access the model and set the current file
        m_Model.setPlagiarisedFile(m_FileChooser.showOpenDialog(m_Stage));

        //  If the current file in the model isn't null
        if (m_Model.getPlagiarisedFile() != null)
        {
            // We can attempt to open the file
            openFile(m_Model.getPlagiarisedFile());
        }

        // We are then loading the text onto the main screen
        m_PlagiarisedField.setText(m_Model.getPlagiarisedText());

        // Retrieving the preprocessor from the model and initialising the parser
        m_Model.getProcessor().initParser(m_Model.getPlagiarisedFile());

        // The parser parses the text and then saves it to the preprocessed files resource
        m_Model.getProcessor().preProcessFile();

        // Gives the file model access to the preprocessed file
        m_FModel.setPreProcessedPlagiarised(m_Model.getProcessor().getPreProcessedFile());



    }

    /**
     * A setter method used to set the current stage the screen is on
     * @param stage The stage of the screen
     */
    public void setStage(Stage stage)
    {
        this.m_Stage =stage;
    }

    /**
     * A method that runs the main plagiarism detection algorithm when the
     * button is pressed
     * @param actionEvent The event that activates the method 'i.e the press of a button'
     */

    public void plagerIt(ActionEvent actionEvent)
    {
        /* Creating an instance of the detector, which now has access to
           the preprocessed files
        */
        m_Detector = new Detector(m_FModel);

        m_Detector.setCodeFragments(m_FModel.getProcessor().getExpressions());

        m_Detector.runDetection();

        // Shows the similarity measure of the code
        showSimilarity();

        this.m_LoadingText.setVisible(true);

        m_FModel.cleanUpFiles();

    }

    /**
     * Opens the file from the selection menu
     * @param file The file being opened by the main screen
     */
    private void openFile(File file)
    {
        // Attempts to open the file from the OS directory
        try
        {
            m_Desktop.open(file);
        }
        catch (IOException e)
        {
            // If there are any errors, or a lack of access privileges an error is thrown
            System.out.println("Error: "+e);

        }

    }

    /**
     * A utility method to show the similarity measure of the code
     * in the form of a popup box
     */
    private void showSimilarity()
    {
        // Creating pop up box
        Alert alert = new Alert(Alert.AlertType.INFORMATION);

        // Setting the title and header of the message box
        alert.setTitle("Detection Status");

        alert.setHeaderText("Similarity measure:");

        alert.setContentText("Based on the patterns found, your code gave a " +
                "similarity measure of : "+m_Detector.getSimilarityScore() +
                "%");

        alert.show();


    }


    /**
     * The method invoked upon the exit button clicked, to close the
     * application.
     * @param actionEvent the actionEvent of the calling button
     */
    public void closeApplication(ActionEvent actionEvent)
    {
        Platform.exit();
    }

}
