package com.g28.plager.Logic;

import com.g28.plager.Models.FileModel;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * The main algorithm which will involve using the algorithm
 * to look for patterns and generate a similarity measure
 *
 * @author Conor Cowley
 * @author Xavier Parnell!
 * @author James Ashenden!
 */
public class Detector
{

    /**
     * A collection of each expression in the program
     * extracted by the parser
     */
    private List<String> m_CodeFragments = new ArrayList<>();

    /**
     * Using a scanner to read the file
     */
    private Scanner m_FileReader;

    /**
     * The preprocessed source code
     */
    private String m_Source;


    /**
     * A prime number which will be used in the main algorithm
     */
     private int m_Prime = 101;

    /**
     * The preprocessed plagiarised code
     */

    private String m_Plagiarised;

    /**
     * The generated similarity measure, interpreted as an Int
     */
    private float m_SimilarityScore = 0;

    /**
     * The model which gives the Detector access to the preprocessed files
     */
    private FileModel m_Model;

    /**
     * The length of the plagiarised code
     */
    private int m_PlagiarisedLength;

    /**
     * The length of the source code
     */

    private int m_SourceLength;

    /**
     * The number of times a pattern hasn't been detected
     */
    private float m_PassCount;

    /**
     * The number of times a pattern has been detected
     */
    private int m_DetectionCount;

    /**
     * T
     * @param model
     */
    public Detector(FileModel model)
    {
        m_Model = model;

        // Retrieving the preprocessed code from the model
        setPlagiarisedCode(m_Model.getPlagiarisedText());
        setSourceCode(m_Model.getSourceText());


        // Initialising the lengths of both patterns
        m_PlagiarisedLength = m_Plagiarised.length();
        m_SourceLength = m_Source.length();

    }


    /**
     * A getter method used to retrieve the similarity score
     * @return The similarity measure, interpreted as an Integer
     */
    public float getSimilarityScore()
    {
        System.out.println("Total Passes"+m_PassCount);

        m_SimilarityScore =  m_DetectionCount/ (m_PassCount + m_DetectionCount);

        return Math.round((m_SimilarityScore * 100));
    }

    /**
     * A setter method used to set the source code from the preprocessed file
     * @param source The source code, interpreted as a String
     */
    public void setSourceCode(String source)
    {
        m_Source = source;
    }

    public void setCodeFragments(List<String> codeFragments)
    {
        m_CodeFragments = codeFragments;

    }

    /**
     * A setter method used to set the plagiarised code from the preprocessed file
     * @param plagiarised The plagiarised code, interpreted as a String
     */
    public void setPlagiarisedCode(String plagiarised)
    {
        m_Plagiarised = plagiarised;
    }

    public void runDetection()
    {
        System.out.println(m_CodeFragments); //Printing empty list currently
       for (String m_codeFragment : m_CodeFragments)
       {
            System.out.println(m_codeFragment);
            rabinKarp(m_codeFragment);
        }
    }


    /**
     * The main method responsible for detecting patterns
     * and generating the similarity measure
     */

    public void rabinKarp(String pattern)
    {
        boolean isDetected =false;
        int plagiarisedHash = 0;

        m_PlagiarisedLength  = pattern.length();

        m_Plagiarised = pattern;

        int numCharsInAlpha = 256;

        int sourceHash = 0;

        int hash = 1;

        int i,j = 0;

        for(i = 0; i<m_PlagiarisedLength-1;i++)
        {
            hash = (hash * numCharsInAlpha) % m_Prime;
        }

        for(i = 0; i<m_PlagiarisedLength;i++)
        {
            plagiarisedHash = (numCharsInAlpha * plagiarisedHash + m_Plagiarised.charAt(i)) % m_Prime;
            sourceHash = (numCharsInAlpha * sourceHash + m_Source.charAt(i)) % m_Prime;

        }

        for( i = 0;i<= m_SourceLength - m_PlagiarisedLength;i++)
        {

            if(plagiarisedHash == sourceHash)
            {
                for( j = 0; j< m_PlagiarisedLength;j++)
                {
                    if(m_Source.charAt(i+j) != m_Plagiarised.charAt(j))
                    {
                        break;

                    }
                }
                if(j == m_PlagiarisedLength)
                {
                    m_DetectionCount++;
                    isDetected = true;

                }
            }
            if(i < m_SourceLength - m_PlagiarisedLength)
            {
                sourceHash = (numCharsInAlpha * (sourceHash - m_Source.charAt(i)* hash)+
                        m_Source.charAt(i + m_PlagiarisedLength)) % m_Prime;

                if(sourceHash < 0)
                {
                    sourceHash = sourceHash + m_Prime;


                }
            }

        }

        if(!isDetected)
             m_PassCount++;

    }


}

