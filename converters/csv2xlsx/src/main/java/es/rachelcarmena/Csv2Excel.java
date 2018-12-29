package es.rachelcarmena;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Iterator;
import java.util.Locale;
import org.apache.poi.ss.usermodel.Cell;
import org.apache.poi.ss.usermodel.CellStyle;
import org.apache.poi.ss.usermodel.CreationHelper;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.streaming.SXSSFWorkbook;

public class Csv2Excel {
    
    public static void main(String argv[]) throws Exception {

        if (argv.length < 1) {
            System.out.println("\nOooops! Use:\n");
            System.out.println("\tjava -jar Csv2Excel.jar source.csv\n");
            System.exit(0);
        }
        try {
            FileReader csvFile = new FileReader(argv[0]);
            int extensionIndex = argv[0].lastIndexOf('.');
            File excelFile = new File(argv[0].substring(0, extensionIndex) + ".xlsx");
            int rowNumber = 0;
            int cellNumber = 0;

            BufferedReader reader = new BufferedReader(csvFile);
            SXSSFWorkbook wb = new SXSSFWorkbook(100);
            CreationHelper createHelper = wb.getCreationHelper();
            Sheet sh = wb.createSheet();
            String line = null;

            SimpleDateFormat dateFormat = new SimpleDateFormat("dd/MM/yyyy");
            CellStyle dateCellStyle = wb.createCellStyle();
            dateCellStyle.setDataFormat(createHelper.createDataFormat().getFormat("dd/MM/yyyy"));
    
            while ((line = reader.readLine()) != null) {

                Row row = sh.createRow(rowNumber);
                String[] data = line.split(";");
                cellNumber = 0;
                for (String singleData: data) {

                    singleData = singleData.trim();
                    Cell cell = row.createCell(cellNumber);
                    if (singleData.matches("^[0-9]+$")) {
                        cell.setCellValue(Integer.valueOf(singleData));
                    } else if (singleData.matches("^[0-9]+\\.[0-9]+$")) {
                        cell.setCellValue(Double.valueOf(singleData));
                    } else if (singleData.matches("^[0-9]{2}/[0-9]{2}/[0-9]{4}$")) {
                        cell.setCellValue(dateFormat.parse(singleData));
                        cell.setCellStyle(dateCellStyle);
                    } else if (singleData.length() == 0) {
                        cell.setCellType(Cell.CELL_TYPE_BLANK);
                    } else {
                        cell.setCellValue(singleData);
                    }
                    cellNumber++;
                }
                rowNumber++;
            }

            FileOutputStream excelStream = new FileOutputStream(excelFile);
            wb.write(excelStream);
            System.out.println("Written!");
            excelStream.close();
            csvFile.close();
            reader.close();
            wb.dispose();
        } 
        catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
