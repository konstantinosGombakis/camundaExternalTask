package com.camunda.externaltask.settingtemperature;

import org.camunda.bpm.client.spring.annotation.ExternalTaskSubscription;
import org.camunda.bpm.client.task.ExternalTask;
import org.camunda.bpm.client.task.ExternalTaskHandler;
import org.camunda.bpm.client.task.ExternalTaskService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;

import java.util.HashMap;
import java.util.Map;

@Component
@ExternalTaskSubscription("setting_temperature")
public class HandlerConfiguration implements ExternalTaskHandler {

    @Override
    public void execute(ExternalTask externalTask, ExternalTaskService externalTaskService) {

        Logger logger = LoggerFactory.getLogger(HandlerConfiguration.class);


        Integer temperature = externalTask.getVariable("temperature");
        temperature = temperature + 10;
        //System.out.println("Raising temperature to: " + temperature);

        Map<String, Object> variables = new HashMap<>();
        variables.put("temperature", temperature);

        externalTaskService.complete(externalTask, variables);

        logger.info("Temperature raised to {}", temperature);


    }

}