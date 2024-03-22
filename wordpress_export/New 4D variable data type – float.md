# New 4D variable data type – float

Now that 4Dv11 SQL supports ` float ` data type; it would be nice to match
that with a ` C_FLOAT ` . Using ` C_REAL ` throws an error for incompatible
assignment at runtime.

I.e. if your database has a field with float data type don’t plan on using it
with native 4D code, and don’t expect the complier to warn you. See my [
feature request ](http://forums.4d.fr/Post//4654031/) with 4D.

    
    
    C_REAL($vr_test)
    ` throws error (from GET LAST ERROR STACK): 54 4DRT Argument types are incompatible.
    $vr_test:=[Table]float_field
    

There is an ` Is Float ` constant to compare to ` GET FIELD PROPERTIES ` data
type return longint.

And while we’re at it, why are [ SQL data type values
](http://kb.4d.com/search/assetid=48694) different from [ ` GET FIELD
PROPERTIES ` data type values ](http://doc.4d.com/4D-Language-
Reference-12/Structure-Access/GET-FIELD-PROPERTIES.301-155336.en.html) .

Posted in Wish List | Tagged 4D , data types , float , sql | 1 Comment 


Original post date: November 11, 2010

Category: Wish List