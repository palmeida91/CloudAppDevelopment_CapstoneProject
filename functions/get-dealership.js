/**
  *
  * main() will be run when you invoke this action
  *
  * @param Cloud Functions actions accept a single parameter, which must be a JSON object.
  *
  * @return The output of this action, which must be a JSON object.
  *
  */

const { CloudantV1 } = require('@ibm-cloud/cloudant');
const { IamAuthenticator } = require('ibm-cloud-sdk-core');
const secret={ 
        "COUCH_URL": "https://7eb1a42b-c1ce-429f-833d-ca419ae431ad-bluemix.cloudantnosqldb.appdomain.cloud", 
        "IAM_API_KEY": "QF_a74B4qr__Nm8kUz8lpetgg04zeqDaWptrWrgqhqCU", 
        "COUCH_USERNAME": "7eb1a42b-c1ce-429f-833d-ca419ae431ad-bluemix" 
        }

async function main(params) {
      const authenticator = new IamAuthenticator({ apikey: secret.IAM_API_KEY })
      const cloudant = CloudantV1.newInstance({
          authenticator: authenticator
      });
      cloudant.setServiceUrl(secret.COUCH_URL);
      try {
        let dbList = await cloudant.postAllDocs({
            db:'dealerships',
            includeDocs: true
        });
        //using map to create the response object with all the states
        const listAllStates = dbList.result.rows.map((x)=>{ return {
        "id": x.doc.id,
        "city": x.doc.city,
        "state": x.doc.state,
        "st": x.doc.st,
        "address": x.doc.address,
        "zip": x.doc.zip,
        "lat": x.doc.lat,
        "long": x.doc.long,
        "short_name": x.doc.short_name,
        "full_name": x.doc.full_name
        }})
        
        //using filter if a select params.state is select
        if (params.state){
            const filterBystate = params.state;
            const listByFilteredSt = listAllStates.filter(item => {
                return item.st===filterBystate
                
            });
            return { listByFilteredSt };
        }
        
          //using filter if a select params.dealerId is select
        if (params.dealerId){
            const filterByDealerId = params.dealerId;
            const listByFilteredId = listAllStates.filter(item =>{return  item.id===filterByDealerId});
            return { listByFilteredId };
        }
        
        return { listAllStates };
        // console.log(dbList);
      } catch (error) {
          return { error: error.description };
      }
      
      
}



