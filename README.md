# detectionsc (Intrusion Detection for System Calls)
Python Scripts for Formatting Data -- Using the ADFA-LD dataset which contains system call traces.

<ul>
  <li>Scripts format the data for evluation using scikitlearn</li>
  <li>Contains a model builder for a support vector machine using the ngrams</li>
</ul>

#Updates

<ul>
  <li>Created a primitive python script to format the normal training data into the arff file</li>
  <li>Began using scikit_learn's libraries to implement the corrected way of using ngramas in classification</li>
  <li>Successfully implemented SVM to be able to classify ngrams</li>
  <li>Moved onto only using SVMs as a means of classification due to performance</li>
  <li>Implemented cross validation with the SVM implementation</li>
  <li>Created a formater for compression versus uncompressed system call traces using ngrams</li>
</ul>

#TO-DO

<ul>
  <li>Implement on a live system to validate results from the model</li>
  <li>Optimization of the classification process during model building</li>
  <li>See the results of having skips in the ngrams</li>
</ul>


