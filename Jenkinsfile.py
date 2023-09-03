pipeline{
 agent any
 stages{
 stage ('build'){
 steps{
 echo " my first pipeline"
 sh 'python --version'
 sh 'python pipeline.y'
 print ('Hi')
 print ('Hi')
}
}
}
}
