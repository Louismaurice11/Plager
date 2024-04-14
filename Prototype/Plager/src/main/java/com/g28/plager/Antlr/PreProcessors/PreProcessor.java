package com.g28.plager.Antlr.PreProcessors;

import java.io.File;
import java.io.IOException;

/**
 * Defines what a PreProcessor must do. For example,
 * it needs a Parser and needs to use the parser to preprocess the file
 *
 * @author Conor Cowley (psycc4)
 */
public abstract class PreProcessor
{
    /**
     * A method that initialises the parser, so it can be used
     * for preprocessing
     * @param path The File that the parser will be using
     * @throws IOException Throws an exception if the file isn't found
     */
    public abstract void initParser(File path) throws IOException;

    /**
     * The main method of the PreProcessor, which involves preprocessing
     * the file
     * @throws IOException Throws an exception if the file isn't found
     */
    public abstract void preProcessFile() throws IOException;
    


}
