/**
 * This file contains all the resources and libraries needed
 * for the prototype
 *
 * @author Conor Cowley
 * @author edited - Xavier Parnell
 */
module Plager
{
    requires java.desktop;
    requires antlr.runtime;
    requires antlr4;
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.media;
    requires javafx.swing;
    requires org.antlr.antlr4.runtime;
    requires java.sql;
    requires mysql.connector.j;
    opens Grammars;
    opens DummyFiles;
    opens Views;
    exports com.g28.plager;
    opens com.g28.plager;
    exports com.g28.plager.Controllers;
    opens com.g28.plager.Controllers;

}