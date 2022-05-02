package
Testing;
import org.openqa.selenium. *;
import org.openqa.selenium.chrome.ChromeDriver;

import org.testng.annotations.Test;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.AfterClass;

public


class DemoLogin {

// driver initialization
private static WebDriver driver;

@ Test
public void Test1() {
driver.get("https://demo.guru99.com/test/newtours/");

driver.findElement(By.name("userName")).sendKeys("admin");

driver.findElement(By.name("password")).sendKeys("admin");

driver.findElement(By.name("submit")).submit();

}

@ BeforeClass
public void beforeClass() {
// set the path of the chrome driver
System.setProperty("webdriver.chrome.driver", "C:\\Users\\ADMIN\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe");
driver=new ChromeDriver();
}

@ AfterClass
public void afterClass() {
driver.close();

}

}