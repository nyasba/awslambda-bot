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

�ł���zip���A�b�v���[�h���āAhandler�́upost_chatwork_at_lambda_with_s3.lambda_handler�v�ɂ���B

EventSource��ǉ���I�сA�ȉ���ݒ肵�ĕۑ�

* EventSourceType�FS3
* Bucket�F�g���K�ɂ�����Bucket
* EventType�F�t�@�C���쐬�^�폜�Ȃǃg���K�ɂ������C�x���g

### S3�Ƀt�@�C����u���Ă݂�

