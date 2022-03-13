#include <iostream>
#include <vector>

using namespace std; //make standard library accessible to use names

class Agent {

Agent::Agent() //agent class constructor

//parameters to change in Agent class include action size(int)
//in order to get an output size for neural network 
//no need to include state size because state size is continuous
//and neural networks will acept the output of CNN instead of
//traditional state size with linear networks input
private:
const typedef int action_size; //private access to action_size
const typedef float state; //private access to the vectorized state
const typedef int batch_size; //batch size for updates to networks
const typedef int buffer_size; //buffer size for replay buffer



public:





    

}

class Environment{

    Environment::Environment() //class constructor for environment
        
        //bearer token string to be used in API calls
        typedef const str bearer_token = "c00f3da14e736b95bce848501bfdea7a-54f731eeda7ba20287dae157a23943ba"
        
        
        
    // Create class for interactions with environment:
        
        
        // Include a function to cue taking a trade (Oanda -> Docs -> Order)
        
            // Parameters for opening Order (/v3/accounts/{accountID}/orders) inlclude:
        
                //Autorization: bearer token (string)
                //Accept-DateTime format:  Date Time formatted in Unix (string)
                //Account ID (string)
        
        // Include a function that returns all positions and balance (v3/accounts/{accountID}/positions):
        // Parse out most recent position
        
            //Parameters for Position (Oanda -> Docs -> Position) (v3/accounts/{accountID}/positions) function include:
        
                //Authorization bearer token (string)
                //path: AccountID (string)
        
        
            //Parameters for Account balance (Oanda -> Docs -> Account) (v3/accounts/{accountID}):
                
                //Authorization bearer token (string) 
                //Accept-DateTime format:  Date Time formatted in Unix (string)
                ///path: AccountID (string)
        
        
}
