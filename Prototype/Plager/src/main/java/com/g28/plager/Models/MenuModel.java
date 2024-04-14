package com.g28.plager.Models;

import com.g28.plager.Antlr.PreProcessors.CPreProcessor;

import javax.swing.text.html.StyleSheet;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Scanner;

/**
 * The menu model holds all the information about the files of the main screen,
 * so they can be preprocessed and used in the main algorithm
 *
 * @author Conor Cowley (psycc4)
 */
public class MenuModel
{
    /**
     * The plagiarised file
     */
    private File m_PlagiarisedFile;

    /**
     * The preprocessor used to preprocess the code
     */
    private static final CPreProcessor m_Processor = new CPreProcessor();

    /**
     * The source file
     */
    private File m_SourceFile;

    /**
     * A getter method used to retrieve the current source file
     * @return The source file, interpreted as a Java NIO File object
     */

    public File getSourceFile()
    {
        return m_SourceFile;
    }
    /**
     * A getter method used to retrieve the current plagiarised file
     * @return The plagiarised file, interpreted as a Java NIO File object
     */
    public File getPlagiarisedFile()
    {
        return m_PlagiarisedFile;
    }

    /**
     * A setter method used to set the current source file to apply preprocessing
     * and detection on
     * @param file The source file
     */
    public void setSourceFile(File file)
    {
        m_SourceFile = file;
    }
    /**
     * A setter method used to set the current plagiarised file to apply preprocessing
     * and detection on
     * @param file The source file
     */
    public void setPlagiarisedFile(File file)
    {
        m_PlagiarisedFile = file;
    }

    /**
     * A utility method used to retrieve text from a file
     * @param file The file, interpreted as a Java NIO File object
     * @return The text, interpreted as a String
     */
    protected String readFromFile(File file)
    {

        try
        {
            return Files.readString(Path.of(file.getPath()));

        }
        catch(Exception e)
        {
            System.out.println("Cant read file");
        }
        return "";

    }


    /**
     * A getter method used to retrieve the code in the source file
     * @return The code, interpreted as a String
     */
    public String getSourceText()
    {
        try
        {
            return readFromFile(m_SourceFile);
        }
        catch(Exception e)
        {
            System.out.println("ERROR: Can't display code");
        }

        return "";
    }


    /**
     * A getter method used to retrieve the code in the plagiarised file
     * @return The code, interpreted as a String
     */
    public String getPlagiarisedText()
    {
        try
        {
            return readFromFile(m_PlagiarisedFile);
        }
        catch(Exception e)
        {
            System.out.println("ERROR: Can't display code");
        }

        return "";
    }

    /**
     * A getter method used to retrieve the current instance of the preprocessor
     * @return The preprocessor
     */
    public CPreProcessor getProcessor()
    {
        return m_Processor;
    }
}
