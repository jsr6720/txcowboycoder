# Java string comparison

Mostly just a ‘duh’ moment by myself.

I was fetching properties out of a database using hibernate objects. In my
test scenario I asked if ` "true" == "true" ` which does work. However a
String object does not always equal a string literal nicely.

    
    
    public class Test {
    
    	public static void main(String args[]) {
    		System.out.println("String comparison");
    		// BAD could be true, but could also be false
    		boolean result = "true" == "true" ? true : false;
    		// GOOD will actually compare the strings, not the objects
    		boolean result2 = hibernate_object.getProperties().get("boolean property").equalsIgnoreCase("true") ? true : false;
    
    		System.out.println(result);
    		System.out.println(result2);
    	}
    }
    

[ String JavaDocs
](http://download.oracle.com/javase/1.4.2/docs/api/java/lang/String.html#equalsIgnoreCase\(java.lang.String\))

Posted in Java | Tagged Java , string comparison | Leave a comment 


Original post date: May 23, 2011

Category: Java