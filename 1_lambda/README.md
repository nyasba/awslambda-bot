## �f�v���C�菇

�ڍׂ̓}�j���A���Q��
http://docs.aws.amazon.com/ja_jp/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html

### requests���W���[����ǉ�

```
pip install requests -t <this directory>
```

### zip���k����

���ꂪ�f�v���C�Ώۂ̃p�b�P�[�W�ƂȂ�B
�i�f�B���N�g���ł͂Ȃ��A�f�B���N�g���̒��g�����k���邱�Ɓj

### lambda�ɓo�^����

�ł���zip���A�b�v���[�h���āAhandler�́upost_chatwork_at_lambda.lambda_handler�v�ɂ���B


### �X�P�W���[���g���K�ɂ���ꍇ��

cron expression�����u0 * * * ? *�v�Ȃǂɂ���
