
/***********************************************************************
*                                                                      *
* OnbotJava Editor is still : beta! Please inform us of any bugs       |
* on our discord channel! https://discord.gg/e7nVjMM                   *
* Only BLOCKS code is submitted when in Arena                          *
*                                                                      *
***********************************************************************/


public class MyFIRSTJavaOpMode extends LinearOpMode {
    DcMotor backLeftDrive;
    DcMotor backRightDrive;
    DcMotor frontLeftDrive;
    DcMotor frontRightDrive;
    DcMotor armTilt;
    DcMotor armExtend;
    DcMotor claw;
    ColorSensor color1;
    DistanceSensor distance1;
    BNO055IMU imu;

var ticks;
    
    // Describe this function...
    public void init(){
      backLeftDrive.setDirection(DcMotor.Direction.REVERSE);
      backLeftDrive.setDirection(DcMotor.Direction.REVERSE);
      stop2();
    }
    
    // Describe this function...
    public void stop2(){
      backLeftDrive.setPower(0);
      backRightDrive.setPower(0);
      frontLeftDrive.setPower(0);
      frontRightDrive.setPower(0);
      backLeftDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
      backRightDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
      frontLeftDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
      frontRightDrive.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
    }
    
    // Describe this function...
    public void turn_90_icu(){
      imu.initialize(new BNO055IMU.Parameters());
      backLeftDrive.setPower(0.3);
      backRightDrive.setPower(-0.3);
      frontLeftDrive.setPower(-0.3);
      frontRightDrive.setPower(-0.3);
      while (opModeIsActive()) {
        if (imu.getAngle() > 90) {
          break;
        }
      }
      stop2();
    }
    
    // Describe this function...
    public void turn_90(){
      backLeftDrive.setPower(-0.3);
      backRightDrive.setPower(-0.3);
      frontLeftDrive.setPower(-0.3);
      frontRightDrive.setPower(-0.3);
      sleep(6000);
      stop2();
    }
    
    // Describe this function...
    public void go_forward(){
      backLeftDrive.setPower(0.3);
      backRightDrive.setPower(0.3);
      frontLeftDrive.setPower(-0.3);
      frontRightDrive.setPower(0.3);
      sleep(2000);
      stop2();
    }
    
    // Describe this function...
    public void go_backward(){
      backLeftDrive.setPower(-0.3);
      backRightDrive.setPower(-0.3);
      frontLeftDrive.setPower(0.3);
      frontRightDrive.setPower(-0.3);
      sleep(3000);
      stop2();
    }
    
    // Describe this function...
    public void go_forward_encoder(String ticks){
      backLeftDrive.setPower(0.3);
      backRightDrive.setPower(0.3);
      frontLeftDrive.setPower(-0.3);
      frontRightDrive.setPower(0.3);
      while (opModeIsActive()) {
        telemetry.addData("position", backLeftDrive.getCurrentPosition());
        telemetry.update();
        if (backLeftDrive.getCurrentPosition() > ticks) {
          break;
        }
      }
      stop2();
    }
    
    
    @Override
    public void runOpMode() {
      backLeftDrive = hardwareMap.get(DcMotor.class, "backLeftDrive");
      backRightDrive = hardwareMap.get(DcMotor.class, "backRightDrive");
      frontLeftDrive = hardwareMap.get(DcMotor.class, "frontLeftDrive");
      frontRightDrive = hardwareMap.get(DcMotor.class, "frontRightDrive");
      armTilt = hardwareMap.get(DcMotor.class, "armTilt");
      armExtend = hardwareMap.get(DcMotor.class, "armExtend");
      claw = hardwareMap.get(DcMotor.class, "claw");
      color1 = hardwareMap.get(ColorSensor.class, "color1");
      distance1 = hardwareMap.get(DistanceSensor.class, "distance1");
      imu = hardwareMap.get(BNO055IMU.class, "imu");
      // Put initialization blocks here
      init();
      waitForStart();
      // Put run blocks here
      go_forward();
      for (int count2 = 0; count2 < 4; count2++) {
        go_forward_encoder(1000);
        turn_90_icu();
      }
      go_backward();
    }
    
}
