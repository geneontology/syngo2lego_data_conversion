import sbt._


object MyBuild extends Build 
  { lazy val root = Project ( "root" , file ( "." )) dependsOn 
                  ( syngo2lego ) 
                  lazy val brainscowl = RootProject (
                      uri ( "git://github.com/geneontology/syngo2lego.git)) }
