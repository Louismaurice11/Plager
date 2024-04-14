package com.g28.plager.Antlr.PreProcessors;

import com.g28.plager.Antlr.Parsers.CParser.CLexer;
import com.g28.plager.Antlr.Parsers.CParser.CListener;
import com.g28.plager.Antlr.Parsers.CParser.CParser;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.ParseTree;
import org.antlr.v4.runtime.tree.ParseTreeWalker;
import org.antlr.v4.runtime.tree.Tree;
import org.antlr.v4.runtime.tree.Trees;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.List;

/** The C Preprocessor class applies the C grammar file, a selection
 *  of standards that define a C program. The class's main functionality is to remove
 *  unnecessary information (preprocessor directives) and parse important information
 *
 * @author Conor Cowley (psycc4)
 */
public class CPreProcessor extends PreProcessor
{
    /** A C parser, as we are using a C preprocessor */
    private CParser m_Parser;

    /** An instance of the file being worked on, so utility methods
     *  have access to it
     */
    private File m_File;

    /**
     * The location of the PreProcessed file
     */
    private File m_PreProcessedFile;


    private String m_Text;
    /**
     * The stream of tokens received by the parser
     */
    private TokenStream m_Token;

    /**
     * A stream rewriter, so the parsed text is rewritten to the file
     * in the correct format
     */

    private TokenStreamRewriter m_Rewriter;


    private ArrayList<String> m_CodeFragments;


    /**
     * A utility method use to set up the parser, so it can begin
     * preprocessing the file
     * @param path The file that the parser will be working on
     */
    public void initParser(File path)
    {
        try
        {
            // Setting the path of the file
            m_File = path;

            // Defining a CharStream object for the parser to use
            CharStream charStream = CharStreams.fromFileName(path.getPath());
            // Using a lexer to define the rules of the parser
            CLexer lexer = new CLexer(charStream);

            // Retrieving the new text
            m_Token = new CommonTokenStream(lexer);

            // Parsing the text
            m_Parser = new CParser(m_Token);

            // Ensuring the parsed text is in the correct format
            m_Rewriter = new TokenStreamRewriter(m_Token);

        }
        catch(Exception e)
        {
            System.out.println("error");
        }


    }

    /**
     * The main functionality of the PreProcessor, which involves retrieving the file,
     * parsing the text, and writing the result to a new file
     * @throws IOException An exception is thrown if the user cannot access the file
     */
    public void preProcessFile() throws IOException
    {

        // Setting up a parse tree to show the structure of the program
        ParseTree parseTree = m_Parser.translationUnit();

        m_Text = parseTree.getText();

        System.out.println("Get expressions called");

        // Creating the preprocessed file to write to
        m_PreProcessedFile = new File("src/main/resources/PreProcessedFiles/"+getName());

       // Checking if the preprocessed file doesn't already exist
       if(m_PreProcessedFile.createNewFile())
        {
            // Call the utility method to write to the file
            writeToFile(m_PreProcessedFile);
        }
        else
        {
            // If it does, notify the user
            System.out.println("Error: File already preprocessed");
        }

    }

    /**
     * A utility method to walk the tree and retrieve each individual expression
     * @return A collection of the expressions, interpreted as an ArrayList of Strings
     */
    public List<String> getExpressions()
    {

        ParseTree T = m_Parser.translationUnit();
        // An arraylist to store the interpreted expressions
        String[] expressions;

        System.out.println(m_File.getPath());
        expressions = m_Text.split(";",m_Text.length());

        for(String s: expressions)
        {
            System.out.println(s);
        }

        return Arrays.asList(expressions);

    }

    /** Utility method to write the preprocessed text to a new file **/
    private void writeToFile(File preProcessedFile) throws IOException
    {
        FileWriter write;
        // Attempt to write the preprocessed code to a new location
        try
        {
            write = new FileWriter(m_PreProcessedFile);

            // Writing the preprocessed code to the file
            write.write(m_Rewriter.getText());
            write.close();

        }
        // Throw an error if the file doesn't exist
        catch(IOException e)
        {
            System.out.println("ERROR: Could not write to the file");

        }

    }

    /**
     * A getter used to retrieve the name of the file being processed
     * @return The file name, as a String object
     */
    public String getName()
    {
        return m_File.getName();
    }


    /**
     * A getter method used to retrieve the preprocessed file
     * @return The preprocessed file, interpreted as a JAVA NIO File object
     */
    public File getPreProcessedFile()
    {
        return m_PreProcessedFile;
    }
    public List<String> getChildren()
    {
       return m_CodeFragments;
    }
}
