package com.g28.plager.Models;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;

/**
 * The File model stores an instance of the preprocessed files (from the preprocessor)
 * for the main algorithm to use
 *
 * @author Conor Cowley
 */
public class FileModel extends MenuModel
{
    /**
     * The preprocessed source file
     */
    private File m_PreProcessedSource;

    /**
     * The preprocessed plagiarised file
     */
    private File m_PreProcessedPlagiarised;


    /**
     * A getter method used to retrieve the code in the preprocessed source file
     * @return The code, interpreted as a String
     */
    @Override
    public String getSourceText()
    {
        try
        {
            return readFromFile(m_PreProcessedSource);
        }
        catch(Exception e)
        {
            System.out.println("ERROR: Can't display code");
        }

        return "";
    }


    /**
     * A getter method used to retrieve the code in the preprocessed plagiarised file
     * @return The code, interpreted as a String
     */
    @Override
    public String getPlagiarisedText()
    {
        try
        {
            return readFromFile(m_PreProcessedPlagiarised);
        }
        catch(Exception e)
        {
            System.out.println("ERROR: Can't display code");
        }

        return "";
    }
    /**
     * A setter method used to set the current instance of the preprocessed file
     * @param source The preprocessed source file, interpreted as a Java NIO File
     */
    public void setPreProcessedSource(File source)
    {
        m_PreProcessedSource = source;
    }
    /**
     * A setter method used to set the current instance of the preprocessed file
     * @param plagiarised The preprocessed plagiarised file, interpreted as a Java NIO File
     */
    public void setPreProcessedPlagiarised(File plagiarised)
    {
        m_PreProcessedPlagiarised = plagiarised;

    }

    /**
     * A utility method to clear the users files after a detection has been made
     */
    public void cleanUpFiles()
    {
        try
        {
            Files.delete(m_PreProcessedPlagiarised.toPath());
            Files.delete(m_PreProcessedSource.toPath());
        }
        catch(Exception e)
        {
            System.out.println("Error: Cannot clea files");
        }
    }




}
