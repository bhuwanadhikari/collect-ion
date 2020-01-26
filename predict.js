
const Clarifai = require('clarifai');

const app = new Clarifai.App({ apiKey: '67ed35e690244348b66e2a7548271910' });

const outputs = app.models.initModel({ id: Clarifai.GENERAL_MODEL, version: "aa7f35c01e0642fda5cf400f543e7c40" })
    .then(generalModel => {
        return generalModel.predict("@@sampleTrain");
    })
    .then(response => {
        var concepts = response['outputs'][0]['data']['concepts']
    })

console.log(outputs)
console.log("done")